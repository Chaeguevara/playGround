//https://icons8.com/icon/ZFKgC5O8ab3K/bar-chart
import { BaseExtension } from "./BaseExtension.js";
import { ToasterUIPanel } from "./ToasterUIPanel.js";

class ToasterExtension extends BaseExtension {
    constructor(viewer, options) {
        super(viewer, options)
        this.extensionName = "ToasterExtension"
        this._barChartButton = null;
        this._pieChartButton = null;
        this._barChartPanel = null;
        this._pieChartPanel = null;
    }

    async load() {
        super.load()
        await Promise.all([
            this.loadScript('https://uicdn.toast.com/chart/latest/toastui-chart.min.js', 'toastui'),
            this.loadStyleSheet('https://uicdn.toast.com/chart/latest/toastui-chart.min.css')
        ]);
        console.log(this.extensionName, " loaded");
        return true
    }

    unload() {
        super.unload();
        for (const button of [this._barChartButton, this._pieChartButton]) {
            this.removeToolbarButton(button)
        }
        this._barChartButton = this._pieChartButton = null;
        for (const panel of [this._barChartPanel, this._pieChartButton]) {
            panel.setVisible(false);
            panel.uninitialize();
        }
        this._barChartPanel = this._pieChartPanel = null;
        console.log(`${this.extensionName} unlaoded.`)
    }

    onToolbarCreated() {
        this._barChartPanel = new ToasterUIPanel(this, 'dashboard-toasterBarChart-panel', 'Property bar chart', { x: 10, y: 10, chartType: 'bar' });

        this._barChartButton = this.createToolbarButton('dashboard-toasterbarchart-button', 'https://img.icons8.com/material-two-tone/24/bar-chart.png', 'Show property by toaster ui');
        this._pieChartButton = this.createToolbarButton('dashboard-toasterpichart-button', 'https://img.icons8.com/fluency-systems-regular/48/statistics.png', 'Show property through pie');
        this._barChartButton.onClick = () => {
            this._barChartPanel.setVisible(!this._barChartPanel.isVisible());
            this._barChartButton.setState(this._barChartPanel.isVisible() ? Autodesk.Viewing.UI.Button.State.ACTIVE : Autodesk.Viewing.UI.Button.State.INACTIVE);
            if(this._barChartPanel.isVisible() && this.viewer.model){
                this._barChartPanel.setModel(this.viewer.model);
            }
        }
    }

    onModelLoaded(model) {

    }
    async findPropertyValueOccurrences(model, propertyName) {
        const dbids = await this.findLeafNodes(model);
        return new Promise((res, rej) => {
            model.getBulkProperties(dbids, { propFilter: [propertyName] }, (results) => {
                let histogram = new Map();
                for (const result of results) {
                    if (result.properties.length> 0) {
                        const key = result.properties[0].displayValue;
                        if (histogram.has(key)) {
                            histogram.get(key).push(result.dbId);
                        } else {
                            histogram.set(key, [result.dbId]);
                        }
                    }
                }
                res(histogram)
            }, rej);
        });
    }
}

Autodesk.Viewing.theExtensionManager.registerExtension(ToasterExtension.name, ToasterExtension)