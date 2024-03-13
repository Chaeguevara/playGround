export class BaseExtension extends Autodesk.Viewing.Extension {
    constructor(viewer, options) {
        super(viewer, options);
        this._onObjectTreeCreated = (ev) => this.onModelLoaded(ev.model);
        this._onSelectionChanged = (ev) => this.onSelectionChanged(ev.model, ev.dbIdArray);
        this._onIsolationChanged = (ev) => this.onIsolationChanged(ev.model, ev.nodeIdArray);
    }

    load() {
        this.viewer.addEventListener(Autodesk.Viewing.OBJECT_TREE_CREATED_EVENT, this._onObjectTreeCreated);
        this.viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this._onSelectionChanged);
        this.viewer.addEventListener(Autodesk.Viewing.ISOLATE_EVENT, this._onIsolationChanged);
        return true;
    }

    unload() {
        this.viewer.removeEventListener(Autodesk.Viewing.OBJECT_TREE_CREATED_EVENT, this._onObjectTreeCreated);
        this.viewer.removeEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this._onSelectionChanged);
        this.viewer.removeEventListener(Autodesk.Viewing.ISOLATE_EVENT, this._onIsolationChanged);
        return true;
    }

    onModelLoaded(model) { }

    onSelectionChanged(model, dbids) { }

    onIsolationChanged(model, dbids) { }

    /**
     * @param {Autodesk.Viewing.model} model 
     * @returns 
     */
    findLeafNodes(model) {
        return new Promise(function (resolve, reject) {
            // Question : If i put array here and push something, then I can get ifc graph?
            model.getObjectTree((tree) => {
                let leaves = [];
                //https://aps.autodesk.com/en/docs/viewer/v7/reference/Private/InstanceTree/
                tree.enumNodeChildren(tree.getRootId(), (dbid) => {
                    if (tree.getChildCount(dbid) === 0) {
                        leaves.push(dbid);
                    }
                }, true /* recursively enumerate children's children as well */);
                resolve(leaves);
            }, reject);
        });
    }

    async findPropertyNames(model) {
        const dbids = await this.findLeafNodes(model);
        return new Promise(function (resolve, reject) {
            model.getBulkProperties(dbids, {}, (results) => {
                let propNames = new Set();
                for (const result of results) {
                    for (const prop of result.properties) {
                        propNames.add(prop.displayName);
                    }
                }
                resolve(Array.from(propNames.values()));
            }, reject);
        });
    }
    createToolbarButton(buttonId, buttonIconUrl, buttonToolTip) {
        let group = this.viewer.toolbar.getControl('dashboard-toolbar-group');
        if (!group) {
            group = new Autodesk.Viewing.UI.ControlGroup('dashboard-toolbar-group');
            this.viewer.toolbar.addControl(group)
        }
        const button = new Autodesk.Viewing.UI.Button(buttonId);
        button.setToolTip(buttonToolTip);
        group.addControl(button);
        const icon = button.container.querySelector('.adsk-button-icon');
        if (icon) {
            icon.style.backgroundImage = `url(${buttonIconUrl})`
            icon.style.backgroundSize = `24px`;
            icon.style.backgroundRepeat = `no-repeat`;
            icon.style.backgroundPosition = `center`;
        }
        return button;
    }

    removeToolbarButton(button) {
        const group = this.viewer.toolbar.getControl('dashboard-toolbar-group');
        group.removeControl(button);
    }

    loadScript(url, namespace) {
        if (window[namespace] !== undefined) {
            return Promise.resolve();
        }
        return new Promise((res, rej) => {
            const el = document.createElement('script');
            el.src = url;
            el.onload = res;
            el.onerror = rej;
            document.head.appendChild(el);
        })
    }

    loadStyleSheet(url){
        return new Promise((res,rej)=>{
            const el = document.createElement('link')
            el.rel = 'stylesheet';
            el.href = url;
            el.onload = res;
            el.onerror = rej;
            document.head.appendChild(el)

        })
    }
}