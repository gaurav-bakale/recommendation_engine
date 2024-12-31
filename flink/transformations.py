def process_stream(stream):
    def map_function(event):
        event["processed"] = True
        return event

    stream.map(map_function).print()