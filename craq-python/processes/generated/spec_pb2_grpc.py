# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import spec_pb2 as spec__pb2


class CoordinatorStub(object):
    """The greeter service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/craq.Coordinator/Register',
                request_serializer=spec__pb2.RegisterRequest.SerializeToString,
                response_deserializer=spec__pb2.RegisterReply.FromString,
                )
        self.Write = channel.unary_unary(
                '/craq.Coordinator/Write',
                request_serializer=spec__pb2.WriteRequest.SerializeToString,
                response_deserializer=spec__pb2.WriteReply.FromString,
                )


class CoordinatorServicer(object):
    """The greeter service definition.
    """

    def Register(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoordinatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=spec__pb2.RegisterRequest.FromString,
                    response_serializer=spec__pb2.RegisterReply.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=spec__pb2.WriteRequest.FromString,
                    response_serializer=spec__pb2.WriteReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'craq.Coordinator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Coordinator(object):
    """The greeter service definition.
    """

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Coordinator/Register',
            spec__pb2.RegisterRequest.SerializeToString,
            spec__pb2.RegisterReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Coordinator/Write',
            spec__pb2.WriteRequest.SerializeToString,
            spec__pb2.WriteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/craq.Node/Read',
                request_serializer=spec__pb2.ReadRequest.SerializeToString,
                response_deserializer=spec__pb2.ReadReply.FromString,
                )
        self.Write = channel.unary_unary(
                '/craq.Node/Write',
                request_serializer=spec__pb2.WriteRequest.SerializeToString,
                response_deserializer=spec__pb2.WriteReply.FromString,
                )


class NodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=spec__pb2.ReadRequest.FromString,
                    response_serializer=spec__pb2.ReadReply.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=spec__pb2.WriteRequest.FromString,
                    response_serializer=spec__pb2.WriteReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'craq.Node', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Node(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Node/Read',
            spec__pb2.ReadRequest.SerializeToString,
            spec__pb2.ReadReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Node/Write',
            spec__pb2.WriteRequest.SerializeToString,
            spec__pb2.WriteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ClientStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/craq.Client/Read',
                request_serializer=spec__pb2.ReadRequest.SerializeToString,
                response_deserializer=spec__pb2.ReadReply.FromString,
                )
        self.Write = channel.unary_unary(
                '/craq.Client/Write',
                request_serializer=spec__pb2.WriteRequest.SerializeToString,
                response_deserializer=spec__pb2.WriteReply.FromString,
                )


class ClientServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=spec__pb2.ReadRequest.FromString,
                    response_serializer=spec__pb2.ReadReply.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=spec__pb2.WriteRequest.FromString,
                    response_serializer=spec__pb2.WriteReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'craq.Client', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Client(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Client/Read',
            spec__pb2.ReadRequest.SerializeToString,
            spec__pb2.ReadReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/craq.Client/Write',
            spec__pb2.WriteRequest.SerializeToString,
            spec__pb2.WriteReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
