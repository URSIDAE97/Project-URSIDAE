export class TrayComponent {

    constructor(win) {

        this.iconPath = '../src/assets/logos/logo_1.png'
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
