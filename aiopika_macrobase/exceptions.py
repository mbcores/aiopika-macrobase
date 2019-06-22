from aio_pika.message import DeliveredMessage


class AiopikaException(Exception):
    requeue = None


class RoutingException(AiopikaException):
    pass


class ContentTypeNotSupportedException(AiopikaException):
    pass


class EndpointNotImplementedException(AiopikaException):
    pass


class ResponseFailedSendException(AiopikaException):
    pass


class SerializeFailedException(AiopikaException):
    requeue = False


class DeserializeFailedException(AiopikaException):
    requeue = False


class IncomingRoutingFailedException(AiopikaException):
    pass


class ResultDeliveryFailedException(AiopikaException):
    requeue = False


class PublishTaskException(AiopikaException):

    def __init__(self, queue: str, task: str, correlation_id: str):
        super(PublishTaskException, self).__init__(f'<Queue: {queue} task: {task} correlation_id: {correlation_id}> Publish task error')


class DeliveryException(AiopikaException):

    def __init__(self, message: DeliveredMessage):
        super(DeliveryException, self).__init__(f'<Exchange: {message.delivery.exchange} routing_key: {message.delivery.routing_key} code: {message.delivery.reply_code}> {message.delivery.reply_text}')


class MessageTimeoutException(AiopikaException):

    def __init__(self, queue: str, task: str, correlation_id: str):
        super(MessageTimeoutException, self).__init__(f'<Queue: {queue} task: {task} correlation_id: {correlation_id}> Service is unavailable')
