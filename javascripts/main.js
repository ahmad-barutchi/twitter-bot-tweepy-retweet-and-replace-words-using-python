console.log('This would be the main JS file.');
navigator.registerProtocolHandler("mailto",
                                  "https://mail.google.com/mail/?extsrc=mailto&url=%s",
                                  "Gmail");
