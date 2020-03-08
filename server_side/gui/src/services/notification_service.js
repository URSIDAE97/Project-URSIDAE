import UIkit from 'uikit'

class NotificationService {

  constructor () {}

  info (message, timeout) {
    UIkit.notification({
      message: message,
      timeout: timeout,
      status: 'primary',
      pos: 'bottom-right'
    })
  }

  success (message, timeout) {
    UIkit.notification({
      message: message,
      timeout: timeout,
      status: 'success',
      pos: 'bottom-right'
    })
  }

  warning (message, timeout) {
    UIkit.notification({
      message: message,
      timeout: timeout,
      status: 'warning',
      pos: 'bottom-right'
    })
  }

  error (message, timeout) {
    UIkit.notification({
      message: message,
      timeout: timeout,
      status: 'danger',
      pos: 'bottom-right'
    })
  }
}

const notificationService = new NotificationService()

export default notificationService
