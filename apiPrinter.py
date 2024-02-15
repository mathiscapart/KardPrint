import uvicorn
from fastapi import FastAPI, HTTPException, Response, status, APIRouter
from starlette.middleware.cors import CORSMiddleware

from projet.PrinterDriver import PrinterDriver

app = FastAPI()
printer_route = APIRouter()
app.include_router(printer_route, prefix="/v1/printer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

printer = PrinterDriver("Xerox Printer", "1200", "plastic", 10, 3)


@app.get("/v1/printer", status_code=200)
async def get_printer():
    return printer.get_printer_info()


@app.get("/v1/printer/ink", status_code=200)
async def get_printer():
    return printer.get_ink_levels()


@app.post("/v1/printer/print", status_code=200)
async def print_printer():
    printer.print()
    return {
        "printer": "print"
    }


@app.post("/v1/printer/spooler/{card_id}", status_code=200)
async def print_printer(card_id, response: Response):
    try:
        if printer.send_card_to_spooler(card_id):
            return {
                'spooler': f'add {card_id}'
            }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            'result': f'{e}'
        }


@app.get("/v1/printer/spooler/first", status_code=200)
async def print_printer():
    return {
        "spooler": f"{printer.get_card_in_spooler()}"
    }


@app.post("/v1/printer/print/{card_id}", status_code=200)
async def print_card(card_id: str, response: Response):
    try:
        printer.get_ink_levels()
        printer.get_card_tray_status()
        printer.send_card_to_spooler(card_id)
        printer.print()
        return {
            "result": "success"
        }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "result": "failure",
            "message": str(e)
        }

    """if printer.get_ink_levels() and printer.get_card_tray_status() and printer.send_data_to_spooler(
            str(card_id)) and printer.print():
        return {
            "result": "success"
        }
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "result": "failure"
        }"""


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
