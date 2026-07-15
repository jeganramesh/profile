from burp import IBurpExtender, IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("PwnFox Colorizer")
        callbacks.registerHttpListener(self)
        print("PwnFox Colorizer loaded")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        # We need to check REQUESTS, not responses
        if not messageIsRequest:
            return

        # Only color Proxy history
        if toolFlag == self._callbacks.TOOL_PROXY:
            request = messageInfo.getRequest()
            analyzed = self._helpers.analyzeRequest(request)
            headers = analyzed.getHeaders()

            for header in headers:
                if header.lower().startswith("x-pwnfox-color:"):
                    color = header.split(":")[1].strip().lower()
                    comment = "[{}]".format(color.upper())
                    messageInfo.setHighlight(color) # Burp takes "red", "cyan" directly
                    messageInfo.setComment(comment)
                    break
