import pandas as pd
from ai.result_processor import ResultProcessor

df = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado"],
    "total": [512, 420, 300]
})

processor = ResultProcessor()

result = processor.process(df)

print(result)