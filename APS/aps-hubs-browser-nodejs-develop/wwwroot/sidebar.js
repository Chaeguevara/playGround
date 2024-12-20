async function getJSON(url) {
    const resp = await fetch(url);
    if (!resp.ok) {
        alert('Could not load tree data. See console for more details.');
        console.error(await resp.text());
        return [];
    }
    return resp.json();
}

function createTreeNode(id, text, icon, children = false) {
    return { id, text, children, itree: { icon } };
}

async function getHubs() {
    const hubs = await getJSON('/api/hubs');
    return hubs.map(hub => createTreeNode(`hub|${hub.id}`, hub.attributes.name, 'icon-hub', true));
}

async function getProjects(hubId) {
    const projects = await getJSON(`/api/hubs/${hubId}/projects`);
    return projects.map(project => createTreeNode(`project|${hubId}|${project.id}`, project.attributes.name, 'icon-project', true));
}

async function getContents(hubId, projectId, folderId = null) {
    const contents = await getJSON(`/api/hubs/${hubId}/projects/${projectId}/contents` + (folderId ? `?folder_id=${folderId}` : ''));
    return contents.map(item => {
        if (item.type === 'folders') {
            return createTreeNode(`folder|${hubId}|${projectId}|${item.id}`, item.attributes.displayName, 'icon-my-folder', true);
        } else {
            return createTreeNode(`item|${hubId}|${projectId}|${item.id}`, item.attributes.displayName, 'icon-item', true);
        }
    });
}

async function getVersions(hubId, projectId, itemId) {
    const versions = await getJSON(`/api/hubs/${hubId}/projects/${projectId}/contents/${itemId}/versions`);
    return versions.map(version => createTreeNode(`version|${version.id}`, version.attributes.createTime, 'icon-version'));
}


export function initTree(selector, onSelectionChanged) {
    // See http://inspire-tree.com
    const tree = new InspireTree({
        data: function (node) {
            if (!node || !node.id) {
                return getHubs();
            } else {
                const tokens = node.id.split('|');
                switch (tokens[0]) {
                    case 'hub': return getProjects(tokens[1]);
                    case 'project': return getContents(tokens[1], tokens[2]);
                    case 'folder': return getContents(tokens[1], tokens[2], tokens[3]);
                    case 'item': return getVersions(tokens[1], tokens[2], tokens[3]);
                    default: return [];
                }
            }
        },
        selection: {
            mode: 'checkbox'
        }
    });
    tree.on('node.click', async function (event, node) {
        event.preventTreeDefault();
        let urnArr = []
        const tokens = node.id.split('|');
        console.log(tokens[1])
        if (tokens[0] === 'version') {
            urnArr.push(tokens[1])
        }
        let idx = 0
        let childNodes = await node.expand();
        // iterate children while expanding it. w/o exapnding, impossible to get children info
        while (idx < childNodes.length) {
            console.log(childNodes.length)
            const cur = childNodes.at(idx)
            if (cur.children) {
                const curC = await cur.expand();
                childNodes = [...childNodes, ...curC]
            } else {
                const tok = cur.id.split('|')
                if (tok[0] === 'version') {
                    urnArr.push(tok[1])
                }
            }
            idx++;
        }
        if (urnArr.length < 1){
            throw new Error("No model under this tree")
        }
        // urn to show on view
        console.log(urnArr)
        console.log('click')
        console.log(node)
        if (node.itree.state.checked) {
            node.uncheck(false)
        } else {
            console.log("check")
            node.check(false)
        }
        // if (tokens[0] === 'version') {
        // onSelectionChanged(tokens[1]);
        // }
        idx = 0
        let filteredUrnArr = []
        while (idx < urnArr.length) {
            const curV = urnArr.at(idx).split('=')[1]
            filteredUrnArr.push(urnArr.at(idx))
            idx += curV
        }
        console.log(filteredUrnArr)
        filteredUrnArr = filteredUrnArr.map(urn => window.btoa(urn).replace(/=/g, ''))
        onSelectionChanged(filteredUrnArr)
        console.log(filteredUrnArr)
    });
    const finalTree = new InspireTreeDOM(tree, { target: selector });
    console.log(selector)
    const parent = document.getElementById(selector.slice(1)).parentNode
    const button = document.createElement("button")
    button.setAttribute('content', 'submit')
    button.textContent = 'Click to load model'
    button.addEventListener('click', () => {
        console.log('cliked')
        console.log(tree)
        // tree.expandDeep()
        const tested = tree.filter(no => {
            console.log(no)
            return no.id.split('|')[0] === 'version'
        })
        const checkedNodes = tree.checked()
        console.log(checkedNodes)
        // const tested = tree.find((node)=>{
        //     console.log(node)
        //     node.id.split('|')[0]==='version'})
        console.log(tested)
    })
    parent.appendChild(button)
    return finalTree;
}
