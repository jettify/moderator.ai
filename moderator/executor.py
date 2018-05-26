from concurrent.futures import ProcessPoolExecutor


async def setup_executor(app, conf):
    n = conf['max_workers']

    executor = ProcessPoolExecutor(num_workers=n)

    async def close_executor(app):
        executor.shutdown()

    app.on_cleanup.append(close_executor)
    app['executor'] = executor
    return executor
