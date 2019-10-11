const electron = require('electron')
const path = require('path')

const app = electron.app
const protocol = electron.protocol
const BrowserWindow = electron.BrowserWindow

const Tray = electron.Tray
const trayIcon = path.join(__dirname, '../src/assets/logos/logo_1.png')
const Menu = electron.Menu

let win = null
let tray = null


protocol.registerSchemesAsPrivileged(
  [{scheme: 'app', privileges: { secure: true, standard: true } }]
)

app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (win === null) {
    //createWindow()
  }
})

app.on('ready', function() {
  win = new BrowserWindow({ 
    width: 800, 
    height: 600, 
    webPreferences: {
      nodeIntegration: true
    }    
  })

  win.hide();
  // if (process.env.WEBPACK_DEV_SERVER_URL) {
  //   // Load the url of the dev server if in development mode
  //   win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
  //   if (!process.env.IS_TEST) win.webContents.openDevTools()
  // } else {
  //   createProtocol('app')
  //   // Load the index.html when not in development
  //   win.loadURL('app://./index.html')
  // }

  win.on('closed', () => {
    win = null
  })
  tray = new Tray(trayIcon)

  let template = [
    {
      label: 'Open app'
    }
  ]

  const ctxMenu = Menu.buildFromTemplate(template)
  tray.setContextMenu(ctxMenu)
  tray.setToolTip('URSIDAE')


  tray.on('double-click', function() {
    win.show()
  })
})

// // Exit cleanly on request from parent process in development mode.
// if (isDevelopment) {
//   if (process.platform === 'win32') {
//     process.on('message', data => {
//       if (data === 'graceful-exit') {
//         app.quit()
//       }
//     })
//   } else {
//     process.on('SIGTERM', () => {
//       app.quit()
//     })
//   }
// }

function createWindow () {
  win = new BrowserWindow({ 
    width: 800, 
    height: 600, 
    webPreferences: {
      nodeIntegration: true
    }    
  })

  win.hide();
  // if (process.env.WEBPACK_DEV_SERVER_URL) {
  //   // Load the url of the dev server if in development mode
  //   win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
  //   if (!process.env.IS_TEST) win.webContents.openDevTools()
  // } else {
  //   createProtocol('app')
  //   // Load the index.html when not in development
  //   win.loadURL('app://./index.html')
  // }

  win.on('closed', () => {
    win = null
  })
}