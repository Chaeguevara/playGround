
const DATAGRID_CONFIG = {
    requiredProps: ['name', 'Volume', 'Level'],
    columns: [
        { title: 'ID', field: 'dbid' },
        { title: 'Name', field: 'name', width: 150 },
        { title: 'Volume', field: 'volume', hozAlign: 'left', formatter: 'progress' },
        { title: 'Level', field: 'level' }
    ],
    groupBy: 'level',
    createRow: (dbid, name, props) => {
        const volume = props.find(p => p.displayName === 'Volume')?.displayValue;
        const level = props.find(p => p.displayName === 'Level' && p.displayCategory === 'Constraints')?.displayValue;
        return { dbid, name, volume, level };
    },
    onRowClick: (row, viewer) => {
        viewer.isolate([row.dbid]);
        viewer.fitToView([row.dbid]);
    }
}

export class DataGridPanel extends Autodesk.Viewing.UI.DockingPanel {

    /**
     * 
     * @param {HTMLElement} extension 
     * @param {string} id 
     * @param {string} title 
     * @param {Autodesk.Viewing.UI.DockingPanelOptions} options 
     */
    constructor(extension, id, title, options) {
        super(extension.viewer.container, id, title, options)
        this.extension = extension;
        this.container.style.left = (options.x || 0) + 'px';
        this.container.style.top = (options.y || 0) + 'px';
        this.container.style.width = (options.width || 500) + 'px';
        this.container.style.height = (options.height || 400) + 'px';
        this.container.style.resize = 'none';
    }
    initialize() {
        this.title = this.createTitleBar(this.titleLabel || this.container.id);
        this.initializeMoveHandlers(this.title);
        this.container.appendChild(this.title);
        this.content = document.createElement("div");
        this.content.style.height = '350px';
        this.content.style.backgroundColor = 'white';
        this.content.innerHTML = `<div class="datagrid-container" style="position: relative; height:350px;"></div>`;
        this.container.appendChild(this.content);
        this.table = new Tabulator('.datagrid-container', {
            height: '100%',
            layout: 'fitColumns',
            columns: DATAGRID_CONFIG.columns,
            groupBy: DATAGRID_CONFIG.groupBy,
            rowClick: (e, row) => DATAGRID_CONFIG.onRowClick(row.getData(), this.extension.viewer)
        });
    }
    update(model, dbids) {
        model.getBulkProperties(dbids, { propFilter: DATAGRID_CONFIG.requiredProps }, (res) => {
            this.table.replaceData(res.map((r) => DATAGRID_CONFIG.createRow(r.dbId,r.name,r.properties)));
        },(err)=>{
            console.error(err);
        });
    }
}