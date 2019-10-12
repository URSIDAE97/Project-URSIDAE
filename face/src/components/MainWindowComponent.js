const path = require('path')

export class MainWindowComponent {

    constructor() {
        this.options = { 
            width: 800, 
            height: 600, 
            webPreferences: {
              nodeIntegration: true
            },
            show: false,
            resizable: false,
            icon: path.join(__dirname, '../src/assets/logos/transparent_white_no_title.png'),
            title: 'URSIDAE'
        }
        
    }

}