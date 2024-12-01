import Versions from './components/Versions'
import electronLogo from './assets/electron.svg'
import ThreeScene from './components/R3F'

function App(): JSX.Element {
  const ipcHandle = (): void => window.electron.ipcRenderer.send('ping')

  return (
    <ThreeScene></ThreeScene>

  )
}

export default App
