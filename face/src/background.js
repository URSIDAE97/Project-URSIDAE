import { TrayComponent } from './components/TrayComponent'

const electron = require('electron')
const path = require('path')

const app = electron.app
const protocol = electron.protocol
const BrowserWindow = electron.BrowserWindow

let win = null
let tray = null

// ----------------------------- //
// -------- Tray module -------- //
// ----------------------------- //

const Tray = electron.Tray
const Menu = electron.Menu
const trayInfo = new TrayComponent(win)
const trayIcon = path.join(__dirname, trayInfo.iconPath)
const trayMenu = Menu.buildFromTemplate(trayInfo.template)

let quit = false


app.on('ready', function() {
  win = new BrowserWindow({ 
    width: 800, 
    height: 600, 
    webPreferences: {
      nodeIntegration: true
    },
    show: false,
    resizable: false,    
  })
  win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)

  win.on('close', (event) => {
    if(!quit) {
      event.preventDefault();
      win.hide()
    }
  })

  tray = new Tray(trayIcon)
  tray.setContextMenu(trayMenu)
  tray.setToolTip('URSIDAE')

  trayMenu.getMenuItemById(trayInfo.OPEN_UI).click = function() {
    win.show()
  }
  trayMenu.getMenuItemById(trayInfo.QUIT).click = function() {
    quit = true
    app.quit()
  }

  tray.on('double-click', function() {
    win.show()
  })

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
