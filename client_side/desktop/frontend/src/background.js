import { TrayComponent } from './components/TrayComponent'
import { MainWindowComponent } from './components/MainWindowComponent'

const Electron = require('electron')

const App = Electron.app
const Protocol = Electron.protocol
const BrowserWindow = Electron.BrowserWindow

let win = null
let tray = null

// ----------------------------- //
// -------- Main window -------- //
// ----------------------------- //

const mainWinInfo = new MainWindowComponent()

let quit = false

// ----------------------------- //
// -------- Tray module -------- //
// ----------------------------- //

const Tray = Electron.Tray
const Menu = Electron.Menu
const trayInfo = new TrayComponent()
const trayMenu = Menu.buildFromTemplate(trayInfo.template)


App.on('ready', function() {
  // --- main window --- //
  win = new BrowserWindow(mainWinInfo.options)
  win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)  

  win.on('close', (event) => {
    if(!quit) {
      event.preventDefault();
      win.hide()
    }
  })

  // --- tray icon --- //
  tray = new Tray(trayInfo.icon)
  tray.setContextMenu(trayMenu)
  tray.setToolTip('URSIDAE')

  tray.on('click', function() {
    win.show()
  })

  trayMenu.getMenuItemById(trayInfo.OPEN_UI).click = function() {
    win.show()
  }
  trayMenu.getMenuItemById(trayInfo.QUIT).click = function() {
    quit = true
    App.quit()
  }

})

Protocol.registerSchemesAsPrivileged(
  [{scheme: 'app', privileges: { secure: true, standard: true } }]
)

App.on('window-all-closed', () => {

})

App.on('activate', () => {

})
