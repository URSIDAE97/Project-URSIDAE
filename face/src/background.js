import { TrayComponent } from './components/TrayComponent'
import { MainWindowComponent } from './components/MainWindowComponent'

const electron = require('electron')

const app = electron.app
const protocol = electron.protocol
const BrowserWindow = electron.BrowserWindow

let win = null
let tray = null

// ----------------------------- //
// -------- Main window -------- //
// ----------------------------- //

const mainWinInfo = new MainWindowComponent()

// ----------------------------- //
// -------- Tray module -------- //
// ----------------------------- //

const Tray = electron.Tray
const Menu = electron.Menu
const trayInfo = new TrayComponent()
const trayMenu = Menu.buildFromTemplate(trayInfo.template)

let quit = false


app.on('ready', function() {
  // --- main window --- //
  win = new BrowserWindow(mainWinInfo.options)
  win.removeMenu()
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
    app.quit()
  }

})

protocol.registerSchemesAsPrivileged(
  [{scheme: 'app', privileges: { secure: true, standard: true } }]
)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {

})
