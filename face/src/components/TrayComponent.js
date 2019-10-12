const path = require('path')

export class TrayComponent {

    constructor() {
        this.icon = path.join(__dirname, '../src/assets/logos/transparent_white_no_title.png'),
        this.template = [
            {
                id: 1,
                label: 'Open UI'
            },
            {
                id: 2,
                label: 'Quit'
            }
        ]        

        this.OPEN_UI = 1
        this.QUIT = 2
    }    
    
}
