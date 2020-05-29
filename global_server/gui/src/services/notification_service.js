import UIkit from 'uikit'

const MAX_COUNT = 5

class NotificationService {
  // this class enables creation of pop up notifications
  // maximal number of notifications that can be displayed set by changing the constant MAX_COUNT

  constructor () {
    this.handles = Array()

    let self = this
    UIkit.util.on(document, 'close', (event) => {
      var idx = self.handles.indexOf(event.detail[0])
      if (idx !== -1) {
        console.log('removed handle')
        self.handles.splice(idx, 1)
      }
    });
  }

  info (message, timeout) {
    this.createNotification('primary', 'info', message, timeout)
  }

  success (message, timeout) {
    this.createNotification('success', 'info', message, timeout)
  }

  warning (message, timeout) {
    this.createNotification('warning', 'warning', message, timeout)
  }

  error (message, timeout) {
    this.createNotification('danger', 'warning', message, timeout)
  }

  createNotification (type, icon, message, timeout) {
    if (this.handles.length < MAX_COUNT) {
      this.handles.push(
        UIkit.notification({
          message: `<span uk-icon=\'icon: ${ icon }\'></span>${ message }`,
          timeout: timeout,
          status: type,
          pos: 'bottom-right'
        })
      )
    } else {
      this.handles[0].close()
      this.handles.splice(0, 1)
      this.createNotification(type, message, timeout)
    }
  }

  closeAll () {
    UIkit.notification.closeAll()
  }
}

const notificationService = new NotificationService()

export default notificationService
