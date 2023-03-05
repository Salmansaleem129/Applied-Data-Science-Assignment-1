import pandas as pd
import matplotlib.pyplot as plt

#Load the data from CSV file
data = pd.read_csv('loan_sanction_test.csv')

#define Function to plot line chart with gender vs loan amount
def line_plot_loanamount():
    #Filter the data by Gender
    male_data = data[data['Gender'] == 'Male']
    female_data = data[data['Gender'] == 'Female']
    
    #Group data by Month and sum the loan amount
    male_group = male_data.groupby('Month')['LoanAmount'].sum()
    female_group = female_data.groupby('Month')['LoanAmount'].sum()
    
    #Plot the line chart for loan amount
    plt.plot(male_group.index, male_group.values, label='Male')
    plt.plot(female_group.index, female_group.values, label='Female')
    plt.xlabel('Month')
    plt.ylabel('Loan Amount (Million)')
    plt.title('Gender vs Loan Amount')
    plt.legend()
    plt.show()

#Define function to plot pie chart of Property Area
def pie_chart_property_area():
    #Group data by Property Area and sum the loan amount
    group_data = data.groupby('Property_Area')['LoanAmount'].sum()
    
    #Plot the pie chart to divide stats of property area
    plt.pie(group_data.values, labels=group_data.index, autopct='%1.1f%%')
    plt.title('Property Area')
    plt.show()

#Define function to plot bar chart of Education Categories vs Loan Amount
def bar_plot_education_For_loanamount():
    #Group data by Education Categories and sum the loan amount
    group_data = data.groupby('Education')['LoanAmount'].sum()
    
    #Plot the bar chart to visualize data education with loan amount
    plt.bar(group_data.index, group_data.values)
    plt.xlabel('Education')
    plt.ylabel('Loan Amount(Million)')
    plt.title('Education vs Loan Amount')
    plt.show()

#Call the functions to generate the plots for visualization
line_plot_loanamount()
pie_chart_property_area()
bar_plot_education_For_loanamount()




