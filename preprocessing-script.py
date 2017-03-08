%%time
# Open data files
path = "./data/"

train = pd.read_csv(path+'train.csv', encoding='iso-8859-1')[::]
test = pd.read_csv(path+'test.csv')
test_ticket_id = np.array(test['ticket_id'])

train = train.set_index('ticket_id')
test = test.set_index('ticket_id')


def preprocess(data, test_set=False):
    # Dropped columns
    drop_cols = [
        # Only found in training set CSV
        'payment_amount',
        'balance_due',
        'payment_date',
        'payment_status',
        'collection_status',
        'compliance_detail',
        # Unhelpful or otherwise
        'inspector_name',
        'violator_name',
        'violation_zip_code',
        'violation_street_number',
        'violation_street_name',
        'mailing_address_str_number',
        'mailing_address_str_name',
        'city',
        'state',
        'zip_code',
        'non_us_str_code',
        'country',
        'violation_description',
        'admin_fee',
        'state_fee',
        'late_fee',
    ]
    drop_col_set = set(drop_cols)
    labels = set(data.columns)
    overlap = drop_col_set & labels
    data.drop(list(overlap), axis=1, inplace=True)

    # Drop the violators who were found not responsible
    if not test_set:
        data.dropna(subset=['compliance'], inplace=True)
    
    # Convert datetime columns into years/months/days
    for column_name in ['ticket_issued_date', 'hearing_date']:
        print('Converting %s to years/months/days...' % column_name)

        # data
        day_time = pd.to_datetime(data[column_name])
        data.drop(column_name, axis=1, inplace=True)
        data[column_name+'_month'] = np.array(day_time.dt.month)
        data[column_name+'_year'] = np.array(day_time.dt.year)
        data[column_name+'_day'] = np.array(day_time.dt.day)
        data[column_name+'_dayofweek'] = np.array(day_time.dt.dayofweek)
        
    # Convert string columns to categorical
    string_cols = data.select_dtypes(exclude=['float', 'int']).columns
    len_train = len(train)

    # Some filtering on violation_code to make it more manageable
    data['violation_code'] = data['violation_code'].apply(lambda x: x.split(' ')[0]).copy()
    data['violation_code'] = data['violation_code'].apply(lambda x: x.split('(')[0]).copy()
    data['violation_code'][data['violation_code'].apply(lambda x: x.find('-')<=0)] = np.nan

    # Make all codes with < 10 occurrences null
    counts = data['violation_code'].value_counts()
    data['violation_code'][data['violation_code'].isin(counts[counts < 10].index)] = np.nan

    for column_name in string_cols:
        print('Converting to categorical...', column_name, '# variables:', len(data[column_name].unique()))
        dummies = pd.get_dummies(data[column_name])
        data[dummies.columns] = dummies
        data.drop(column_name, axis=1, inplace=True)


    features = list( data.columns )
    target = ['compliance']

    print("Number of features:", len(features))
    print

    return data.copy(deep=True)

train = preprocess(train)
test = preprocess(test, test_set=True)