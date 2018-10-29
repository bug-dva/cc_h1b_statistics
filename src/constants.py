class ColumnNameList:
    """
    Since each year of data can have different columns, below three lists collected the SOC_Name, State and Status
    column names from 2008 to 2018 File Structure docs.
    """

    SOC_NAME_COLUMN_NAME_LIST = ['SOC_NAME', 'LCA_CASE_SOC_NAME', 'Occupational_Title']
    STATE_COLUMN_NAME_LIST = ['WORKSITE_STATE', 'LCA_CASE_WORKLOC1_STATE', 'State_1']
    STATUS_COLUMN_NAME_LIST = ['CASE_STATUS', 'STATUS', 'Approval_Status']


class CaseStatusList:
    """
    Below list collected certified case status descriptions from 2008 to 2018 File Structure docs.
    """

    CERTIFIED_CASE_STATUS_LIST = ['CERTIFIED', 'Certified', 'certified']


class OutputFileHeader:
    """
    Below list collected output file headers.
    """
    TOP_10_OCCUPATION = 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'
    TOP_10_STATE = 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'
