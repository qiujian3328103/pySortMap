def convert_data_to_dict(data, groupby_list, subset_list):
    """
    summarize and convert the dataframe as dictionary

    {"lot_1":(wafer_id_1, wafer_alias_2)}

    :param data: data frame
    :return: rest_dict
    {
        lot_id: [
            (number_of_wafers, (wafer_id_1, wafer_number_1)),
            (number_of_wafers, (wafer_id_2, wafer_number_2)),
            (number_of_wafers, (wafer_id_3, wafer_number_3)),
            (number_of_wafers, (wafer_id_4, wafer_number_4))
            ]
    }
    """
    if data.empty:
        return {}
    else:
        dropped_data = data.drop_duplicates(subset=subset_list, keep="first")
        rest_dict = dropped_data.groupby(groupby_list)[subset_list].apply(
            lambda g: list(map(tuple, g.values.tolist()))).to_dict()
        # dropped_data = data.drop_duplicates(subset=['VENDOR_SCRIBE', 'WAFER_NUMBER'], keep="first")
        # rest_dict = dropped_data.groupby(groupby_list)[['VENDOR_SCRIBE', 'WAFER_NUMBER']].apply(
        #     lambda g: list(map(tuple, g.values.tolist()))).to_dict()

    return rest_dict


def filter_bin_data(data, **kwargs):
    """
    filter the dataframe to sub dataframe for
    :param data: dataframe type, raw data of the each die info
    :param **kwargs: filter information

    {
        "WAFER_NUMBER": []
        "VENDOR_SCRIBE": []
        "BIN_NUMBER":[]
    }

    :return: order sub dataframe
    """

    for key, value in kwargs.items():
        pass
    return