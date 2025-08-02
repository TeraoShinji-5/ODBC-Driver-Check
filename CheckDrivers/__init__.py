import azure.functions as func
import pyodbc
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # 利用可能なドライバー一覧
        drivers = pyodbc.drivers()
        
        # SQL Server ドライバーを特定
        sql_drivers = [d for d in drivers if 'SQL Server' in d]
        
        result = {
            "all_drivers": list(drivers),
            "sql_server_drivers": sql_drivers
        }
        
        logging.info(f"Available ODBC drivers: {result}")
        return func.HttpResponse(str(result))
        
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)