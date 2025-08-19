import marimo

__generated_with = "0.8.0"
app = marimo.App(width="medium")


@app.cell
def __():
    # Authors: 23f3000048@ds.study.iitm.ac.in, 23f2004391@ds.study.iitm.ac.in
    # Interactive Data Analysis with Marimo
    # This notebook demonstrates reactive programming with variable dependencies
    
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from datetime import datetime, timedelta
    
    mo.md("""
    # Interactive Data Analysis with Marimo
    
    **Authors:**   
    - 23f2004391@ds.study.iitm.ac.in  

    **Date:** August 16, 2025
    """)
    return datetime, go, mo, np, pd, px, timedelta
