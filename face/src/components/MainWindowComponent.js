const Path = require('path')

export class MainWindowComponent {

    constructor() {
        this.options = { 
            width: 800, 
            height: 600, 
            webPreferences: {
              nodeIntegration: true,
              webSecurity: false
            },
            show: false,
            resizable: false,
            frame: false,
            icon: Path.join(__dirname, '../src/assets/logos/transparent_white_no_title.png'),
            title: 'URSIDAE'
        }
        
    }

}