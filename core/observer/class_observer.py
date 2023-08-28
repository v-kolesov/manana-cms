class Observer:
    def __init__(self):
        self.listeners = {}  # Dictionary to store event listeners
        self.before_hooks = {}  # Dictionary to store before hooks for events
        self.after_hooks = {}  # Dictionary to store after hooks for events

    def listener(self, event):
        def decorator(func):
            """
            Decorator method to add a listener function for a specific event.

            Args:
                event (str): The event to listen for.

            Returns:
                func: The original function, with the added listener.
            """
            if event not in self.listeners:
                self.listeners[event] = []
            self.listeners[event].append(func)
            return func
        return decorator

    def hook(self, timing, event):
        def decorator(func):
            """
            Decorator method to add a hook function for a specific event and timing.

            Args:
                timing (str): "before" or "after" the event.
                event (str): The event to hook into.

            Returns:
                func: The original function, with the added hook.
            """
            hooks = self.before_hooks if timing == "before" else self.after_hooks
            if event not in hooks:
                hooks[event] = []
            hooks[event].append(func)
            return func
        return decorator

    def observe(self, event):
        def decorator(func):
            """
            Decorator method to observe an event and execute associated hooks and listeners.

            Args:
                event (str): The event to observe.

            Returns:
                wrapper: A wrapped version of the original function with hooks and listeners.
            """
            @self.listener(event)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                for before_hook in self.before_hooks.get(event, []):
                    result = before_hook(*args, **kwargs)
                for after_hook in self.after_hooks.get(event, []):
                    result = after_hook(*args, **kwargs)
                return result
            return wrapper
        return decorator


