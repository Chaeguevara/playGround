export class ToasterUIPanel extends Autodesk.Viewing.UI.DockingPanel{
    constructor(extension,id,title,options) {
        super(extension.viewer.container,id,title,options);
        this.extension = extension;
        this.container.style.left = (options.x||0) +'px';
        this.container.style.top = (options.y || 0) + 'px';
        this.container.style.width = (options.width || 700) + 'px';
        this.container.style.height = (options.height || 500) + 'px';
        this.container.style.resize = 'none';
        this.chartType = options.chartType || 'bar';
        this.chart = this.createChart();
    }
    initialize(){
        this.title = this.createTitleBar(this.titleLabel || this.container.id);
        this.initializeMoveHandlers(this.title);
        this.container.appendChild(this.title);
        this.content = document.createElement('div');
        this.content.style.height = '350px';
        this.content.style.backgroundColor = 'white';
        this.content.innerHTML = `
        <div class="props-container" style="position: relative; height:25px; padding: 0.5em;">
            <select class="props"></select>
        </div>
        <div class="chart-container" style="position: relative; height:325px; padding: 0.5em;">
            <div class="chart"></div>
        </div>
        `
        this.select = this.content.querySelector('select.props');
        this.canvas = this.content.querySelector('div.chart');
        this.container.appendChild(this.content);
    }
    createChart(){
        console.log(toastui)
        console.log(toastui.Chart.barChart)
        console.log(this.canvas)
        return toastui.Chart.barChart({
            el:this.canvas,
            data: {
                categories: [],
                series:[]
            },
            options:{
                chart:{width:700,height:400},
                series:{
                    selectable:true
                }
            }
        })
    }

    async setModel(model){
        const propertyNames = await this.extension.findPropertyNames(model);
        this.select.innerHTML = propertyNames.map(prop => `<option value="${prop}">${prop}</option>`).join('\n')
        this.select.onchange = () => this.updateChart(model,this.select.value);
        this.updateChart(model,this.select.value)
    }
    async updateChart(model, propName){
        console.log(this.extension)
        const histogram = await this.extension.findPropertyValueOccurrences(model,propName);
        const propertyValues = Array.from(histogram.keys());
        console.log(this.chart)
        const categories= propertyValues;
        let dataset = {categories:[propName],
        series:[]}
        

        const newData = propertyValues.map((val,idx) => {
            let data = {}
            data['name'] = val
            data['data']= [histogram.get(val).length]
            return data
        })

        console.log(newData)
        // dataset.name = propName;
        // dataset.data = propertyValues.map(val => histogram.get(val).length);
        dataset.series = newData
        this.chart.setData(dataset)
        console.log(this.chart)
        // this.chart.update();
        this.chart.on('selectSeries', (info)=>{
            console.log(info.bar);
            const dbids = histogram.get(info.bar[0].data.label)
            this.extension.viewer.isolate(dbids);
            this.extension.viewer.fitToView(dbids);
        })

        // this.chart.config.options.onClick = (ev,items) =>{
        //     if(items.length === 1){
        //         const index = items[0].index;
        //         const dbids = histogram.get(propertyValues[index]);
        //         this.extension.viewer.isolate(dbids);
        //         this.extension.viewer.fitToView(dbids)
        //     }
        // }

    }

}