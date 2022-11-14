{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNTkXL2odnVYjEBZA5JF9f/"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":339},"id":"ELpGpF6XfRwq","executionInfo":{"status":"error","timestamp":1668401690406,"user_tz":180,"elapsed":24,"user":{"displayName":"Andréia Gonçalves","userId":"00867024157318937005"}},"outputId":"347ac6a5-be45-4139-b6b4-52f01f0e97c0"},"outputs":[{"output_type":"error","ename":"ModuleNotFoundError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)","\u001b[0;32m<ipython-input-1-008ef914b7ad>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgraph_objects\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mgo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'","","\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"],"errorDetails":{"actions":[{"action":"open_url","actionText":"Open Examples","url":"/notebooks/snippets/importing_libraries.ipynb"}]}}],"source":["import streamlit as st\n","import plotly.graph_objects as go\n","import numpy as np"]},{"cell_type":"code","source":["st.set_page_config(\n","    page_title=\"Salários TI CAGED\")\n","\n","st.title(\"Salários TI CAGED\")"],"metadata":{"id":"is8fWglDfg-K"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["streamlit run cagedti2.py"],"metadata":{"id":"IJYV1bBVgHzJ"},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":["# Original"],"metadata":{"id":"W_eCKeGmlI7g"}},{"cell_type":"code","source":["import streamlit as st\n","import plotly.graph_objects as go\n","import numpy as np\n","\n","st.set_page_config(\n","    page_title=\"Previsão de Salário TI no CAGED 2022 \")\n","\n","st.title(\"Previsão de Salário TI no CAGED 2022\")\n","\n","st.header(\"**Monthly Income**\")\n","st.subheader(\"Salary\")\n","colAnnualSal, colTax = st.beta_columns(2)\n","\n","with colAnnualSal:\n","    salary = st.number_input(\"Enter your annual salary($): \", min_value=0.0, format='%f')\n","with colTax:\n","    tax_rate = st.number_input(\"Enter your tax rate(%): \", min_value=0.0, format='%f')\n","\n","tax_rate = tax_rate / 100.0\n","salary_after_taxes = salary * (1 - tax_rate)\n","monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)\n","\n","st.header(\"**Monthly Expenses**\")\n","colExpenses1, colExpenses2 = st.beta_columns(2)\n","\n","with colExpenses1:\n","    st.subheader(\"Monthly Rental\")\n","    monthly_rental = st.number_input(\"Enter your monthly rental($): \", min_value=0.0,format='%f' )\n","    \n","    st.subheader(\"Daily Food Budget\")\n","    daily_food = st.number_input(\"Enter your daily food budget ($): \", min_value=0.0,format='%f' )\n","    monthly_food = daily_food * 30\n","    \n","    st.subheader(\"Monthly Unforeseen Expenses\")\n","    monthly_unforeseen = st.number_input(\"Enter your monthly unforeseen expenses ($): \", min_value=0.0,format='%f' ) \n","    \n","with colExpenses2:\n","    st.subheader(\"Monthly Transport\")\n","    monthly_transport = st.number_input(\"Enter your monthly transport fee ($): \", min_value=0.0,format='%f' )   \n","    \n","    st.subheader(\"Monthly Utilities Fees\")\n","    monthly_utilities = st.number_input(\"Enter your monthly utilities fees ($): \", min_value=0.0,format='%f' )\n","    \n","    st.subheader(\"Monthly Entertainment Budget\")\n","    monthly_entertainment = st.number_input(\"Enter your monthly entertainment budget ($): \", min_value=0.0,format='%f' )   \n","\n","monthly_expenses = monthly_rental + monthly_food + monthly_transport + monthly_entertainment + monthly_utilities + monthly_unforeseen\n","monthly_savings = monthly_takehome_salary - monthly_expenses \n","\n","st.header(\"**Savings**\")\n","st.subheader(\"Monthly Take Home Salary: $\" + str(round(monthly_takehome_salary,2)))\n","st.subheader(\"Monthly Expenses: $\" + str(round(monthly_expenses, 2)))\n","st.subheader(\"Monthly Savings: $\" + str(round(monthly_savings, 2)))\n","\n","st.markdown(\"---\")\n","\n","st.header(\"**Forecast Savings**\")\n","colForecast1, colForecast2 = st.beta_columns(2)\n","with colForecast1:\n","    st.subheader(\"Forecast Year\")\n","    forecast_year = st.number_input(\"Enter your forecast year (Min 1 year): \", min_value=0,format='%d')\n","    forecast_months = 12 * forecast_year \n","    \n","    st.subheader(\"Annual Inflation Rate\")\n","    annual_inflation = st.number_input(\"Enter annual inflation rate (%): \", min_value=0.0,format='%f')\n","    monthly_inflation = (1+annual_inflation)**(1/12) - 1\n","    cumulative_inflation_forecast = np.cumprod(np.repeat(1 + monthly_inflation, forecast_months))\n","    forecast_expenses = monthly_expenses*cumulative_inflation_forecast\n","with colForecast2:\n","    st.subheader(\"Annual Salary Growth Rate\")\n","    annual_growth = st.number_input(\"Enter your expected annual salary growth (%): \", min_value=0.0,format='%f')\n","    monthly_growth = (1 + annual_growth) ** (1/12) - 1\n","    cumulative_salary_growth = np.cumprod(np.repeat(1 + monthly_growth, forecast_months))\n","    forecast_salary = monthly_takehome_salary * cumulative_salary_growth \n","    \n","forecast_savings = forecast_salary - forecast_expenses \n","cumulative_savings = np.cumsum(forecast_savings)\n","\n","x_values = np.arange(forecast_year + 1)\n","\n","fig = go.Figure()\n","fig.add_trace(\n","        go.Scatter(\n","            x=x_values, \n","            y=forecast_salary,\n","            name=\"Forecast Salary\"\n","        )\n","    )\n","\n","fig.add_trace(\n","        go.Scatter(\n","            x=x_values,\n","            y=forecast_expenses,\n","            name= \"Forecast Expenses\"\n","        )\n","    )\n","\n","fig.add_trace(\n","        go.Scatter(\n","                x=x_values, \n","                y=cumulative_savings,\n","                name= \"Forecast Savings\"\n","            )\n","    )\n","fig.update_layout(title='Forecast Salary, Expenses & Savings Over the Years',\n","                   xaxis_title='Year',\n","                   yaxis_title='Amount($)')\n","\n","st.plotly_chart(fig, use_container_width=True)\n","\n"],"metadata":{"id":"iV17vbculMY-"},"execution_count":null,"outputs":[]}]}