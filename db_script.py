from openpyxl import Workbook, load_workbook

def readDoc():
    wb = load_workbook('db.xlsx')
    ws = wb[wb.sheetnames[0]]
    x = list(ws.rows)
    # Read columns and rows
    cols_data = x[0]
    rows_data = x[1:]
    # Create dict
    bulk = db[args.collection].initialize_ordered_bulk_op()
    for row in rows_data:
        pre_dataset = {}
        for idx, r in enumerate(list(row)):
            if r.value is not None:
                t = type(r.value)
                if t == long or t == float:
                    r.value = int(r.value)
                elif t.__name__ == 'datetime':
                    r.value = r.value.strftime('%d/%m/%Y')

                pre_dataset[cols_data[idx].value] = r.value

    # Create new collection
    try:
        bulk.execute()
        message = {
            "status": 201,
            "message": "Created"
        }
    except BulkWriteError:
        message["message"] = "Execution Failed"




if __name__ == "__main__":
    readDoc()
