from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/DBX2Target": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/DBX2Target-1.0-py3-none-any.whl", 
    "pipelines/SQLScript": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SQLScript-1.0-py3-none-any.whl", 
    "pipelines/Streamer": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/Streamer-1.0-py3-none-any.whl", 
    "pipelines/TestJSON": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/TestJSON-1.0-py3-none-any.whl", 
    "pipelines/customers_orders": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customers_orders-1.0-py3-none-any.whl", 
    "pipelines/demo_new": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/demo_new-1.0-py3-none-any.whl", 
    "pipelines/farmers-markets-irs": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/farmers_markets_irs-1.0-py3-none-any.whl", 
    "pipelines/join_agg_sort": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/join_agg_sort-1.0-py3-none-any.whl", 
    "pipelines/sales_view": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/sales_view-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {
    "pipelines/SQLScript": "SQLScript", 
    "pipelines/Streamer": "Streamer", 
    "pipelines/demo_new": "demo_new", 
    "pipelines/join_agg_sort": "join_agg_sort", 
    "pipelines/DBX2Target": "DBX2Target", 
    "pipelines/customers_orders": "customers_orders", 
    "pipelines/sales_view": "sales_view", 
    "pipelines/TestJSON": "TestJSON", 
    "pipelines/farmers-markets-irs": "farmers-markets-irs"
}
