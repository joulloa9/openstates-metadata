from ..models import State, Chamber, District, simple_numbered_districts

NH = State(
    name="New Hampshire",
    abbr="NH",
    capital="Concord",
    capital_tz="America/New_York",
    fips="33",
    unicameral=False,
    legislature_name="New Hampshire General Court",
    division_id="ocd-division/country:us/state:nh",
    jurisdiction_id="ocd-jurisdiction/country:us/state:nh/government",
    url="http://gencourt.state.nh.us",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        num_seats=400,
        title="Representative",
        districts=[
            District(
                "Belknap 1",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:belknap_1",
            ),
            District(
                "Belknap 2",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:belknap_2",
            ),
            District(
                "Belknap 3",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:belknap_3",
            ),
            District(
                "Belknap 4",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:belknap_4",
            ),
            District(
                "Belknap 5",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:belknap_5",
            ),
            District(
                "Belknap 6",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:belknap_6",
            ),
            District(
                "Belknap 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:belknap_7",
            ),
            District(
                "Belknap 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:belknap_8",
            ),
            District(
                "Belknap 9",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:belknap_9",
            ),
            District(
                "Carroll 1",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:carroll_1",
            ),
            District(
                "Carroll 2",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:carroll_2",
            ),
            District(
                "Carroll 3",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:carroll_3",
            ),
            District(
                "Carroll 4",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:carroll_4",
            ),
            District(
                "Carroll 5",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:carroll_5",
            ),
            District(
                "Carroll 6",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:carroll_6",
            ),
            District(
                "Carroll 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:carroll_7",
            ),
            District(
                "Carroll 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:carroll_8",
            ),
            District(
                "Cheshire 1",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:cheshire_1",
            ),
            District(
                "Cheshire 2",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_2",
            ),
            District(
                "Cheshire 3",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_3",
            ),
            District(
                "Cheshire 4",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_4",
            ),
            District(
                "Cheshire 5",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_5",
            ),
            District(
                "Cheshire 6",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_6",
            ),
            District(
                "Cheshire 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_7",
            ),
            District(
                "Cheshire 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_8",
            ),
            District(
                "Cheshire 9",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:cheshire_9",
            ),
            District(
                "Cheshire 10",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_10",
            ),
            District(
                "Cheshire 11",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:cheshire_11",
            ),
            District(
                "Cheshire 12",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:cheshire_12",
            ),
            District(
                "Cheshire 13",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_13",
            ),
            District(
                "Cheshire 14",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_14",
            ),
            District(
                "Cheshire 15",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:cheshire_15",
            ),
            District(
                "Cheshire 16",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:cheshire_16",
            ),
            District(
                "Coos 1", "lower", 2, "ocd-division/country:us/state:nh/sldl:coos_1"
            ),
            District(
                "Coos 2", "lower", 1, "ocd-division/country:us/state:nh/sldl:coos_2"
            ),
            District(
                "Coos 3", "lower", 3, "ocd-division/country:us/state:nh/sldl:coos_3"
            ),
            District(
                "Coos 4", "lower", 1, "ocd-division/country:us/state:nh/sldl:coos_4"
            ),
            District(
                "Coos 5", "lower", 1, "ocd-division/country:us/state:nh/sldl:coos_5"
            ),
            District(
                "Coos 6", "lower", 1, "ocd-division/country:us/state:nh/sldl:coos_6"
            ),
            District(
                "Coos 7", "lower", 1, "ocd-division/country:us/state:nh/sldl:coos_7"
            ),
            District(
                "Grafton 1",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:grafton_1",
            ),
            District(
                "Grafton 2",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_2",
            ),
            District(
                "Grafton 3",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_3",
            ),
            District(
                "Grafton 4",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_4",
            ),
            District(
                "Grafton 5",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_5",
            ),
            District(
                "Grafton 6",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_6",
            ),
            District(
                "Grafton 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_7",
            ),
            District(
                "Grafton 8",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:grafton_8",
            ),
            District(
                "Grafton 9",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:grafton_9",
            ),
            District(
                "Grafton 10",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_10",
            ),
            District(
                "Grafton 11",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_11",
            ),
            District(
                "Grafton 12",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:grafton_12",
            ),
            District(
                "Grafton 13",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:grafton_13",
            ),
            District(
                "Grafton 14",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_14",
            ),
            District(
                "Grafton 15",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_15",
            ),
            District(
                "Grafton 16",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_16",
            ),
            District(
                "Grafton 17",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:grafton_17",
            ),
            District(
                "Hillsborough 1",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_1",
            ),
            District(
                "Hillsborough 2",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_2",
            ),
            District(
                "Hillsborough 3",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:hillsborough_3",
            ),
            District(
                "Hillsborough 4",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_4",
            ),
            District(
                "Hillsborough 5",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_5",
            ),
            District(
                "Hillsborough 6",
                "lower",
                5,
                "ocd-division/country:us/state:nh/sldl:hillsborough_6",
            ),
            District(
                "Hillsborough 7",
                "lower",
                6,
                "ocd-division/country:us/state:nh/sldl:hillsborough_7",
            ),
            District(
                "Hillsborough 8",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_8",
            ),
            District(
                "Hillsborough 9",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_9",
            ),
            District(
                "Hillsborough 10",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_10",
            ),
            District(
                "Hillsborough 11",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_11",
            ),
            District(
                "Hillsborough 12",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_12",
            ),
            District(
                "Hillsborough 13",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_13",
            ),
            District(
                "Hillsborough 14",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_14",
            ),
            District(
                "Hillsborough 15",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_15",
            ),
            District(
                "Hillsborough 16",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_16",
            ),
            District(
                "Hillsborough 17",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_17",
            ),
            District(
                "Hillsborough 18",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_18",
            ),
            District(
                "Hillsborough 19",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_19",
            ),
            District(
                "Hillsborough 20",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_20",
            ),
            District(
                "Hillsborough 21",
                "lower",
                8,
                "ocd-division/country:us/state:nh/sldl:hillsborough_21",
            ),
            District(
                "Hillsborough 22",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_22",
            ),
            District(
                "Hillsborough 23",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:hillsborough_23",
            ),
            District(
                "Hillsborough 24",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_24",
            ),
            District(
                "Hillsborough 25",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_25",
            ),
            District(
                "Hillsborough 26",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_26",
            ),
            District(
                "Hillsborough 27",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_27",
            ),
            District(
                "Hillsborough 28",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_28",
            ),
            District(
                "Hillsborough 29",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_29",
            ),
            District(
                "Hillsborough 30",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_30",
            ),
            District(
                "Hillsborough 31",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_31",
            ),
            District(
                "Hillsborough 32",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_32",
            ),
            District(
                "Hillsborough 33",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_33",
            ),
            District(
                "Hillsborough 34",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_34",
            ),
            District(
                "Hillsborough 35",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_35",
            ),
            District(
                "Hillsborough 36",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_36",
            ),
            District(
                "Hillsborough 37",
                "lower",
                11,
                "ocd-division/country:us/state:nh/sldl:hillsborough_37",
            ),
            District(
                "Hillsborough 38",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_38",
            ),
            District(
                "Hillsborough 39",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:hillsborough_39",
            ),
            District(
                "Hillsborough 40",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:hillsborough_40",
            ),
            District(
                "Hillsborough 41",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:hillsborough_41",
            ),
            District(
                "Hillsborough 42",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_42",
            ),
            District(
                "Hillsborough 43",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:hillsborough_43",
            ),
            District(
                "Hillsborough 44",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_44",
            ),
            District(
                "Hillsborough 45",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:hillsborough_45",
            ),
            District(
                "Merrimack 1",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_1",
            ),
            District(
                "Merrimack 2",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_2",
            ),
            District(
                "Merrimack 3",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_3",
            ),
            District(
                "Merrimack 4",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_4",
            ),
            District(
                "Merrimack 5",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_5",
            ),
            District(
                "Merrimack 6",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_6",
            ),
            District(
                "Merrimack 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_7",
            ),
            District(
                "Merrimack 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_8",
            ),
            District(
                "Merrimack 9",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_9",
            ),
            District(
                "Merrimack 10",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:merrimack_10",
            ),
            District(
                "Merrimack 11",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_11",
            ),
            District(
                "Merrimack 12",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_12",
            ),
            District(
                "Merrimack 13",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_13",
            ),
            District(
                "Merrimack 14",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_14",
            ),
            District(
                "Merrimack 15",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_15",
            ),
            District(
                "Merrimack 16",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_16",
            ),
            District(
                "Merrimack 17",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_17",
            ),
            District(
                "Merrimack 18",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_18",
            ),
            District(
                "Merrimack 19",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_19",
            ),
            District(
                "Merrimack 20",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:merrimack_20",
            ),
            District(
                "Merrimack 21",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_21",
            ),
            District(
                "Merrimack 22",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_22",
            ),
            District(
                "Merrimack 23",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:merrimack_23",
            ),
            District(
                "Merrimack 24",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:merrimack_24",
            ),
            District(
                "Merrimack 25",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_25",
            ),
            District(
                "Merrimack 26",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_26",
            ),
            District(
                "Merrimack 27",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:merrimack_27",
            ),
            District(
                "Merrimack 28",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_28",
            ),
            District(
                "Merrimack 29",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:merrimack_29",
            ),
            District(
                "Rockingham 1",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_1",
            ),
            District(
                "Rockingham 2",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:rockingham_2",
            ),
            District(
                "Rockingham 3",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:rockingham_3",
            ),
            District(
                "Rockingham 4",
                "lower",
                5,
                "ocd-division/country:us/state:nh/sldl:rockingham_4",
            ),
            District(
                "Rockingham 5",
                "lower",
                7,
                "ocd-division/country:us/state:nh/sldl:rockingham_5",
            ),
            District(
                "Rockingham 6",
                "lower",
                10,
                "ocd-division/country:us/state:nh/sldl:rockingham_6",
            ),
            District(
                "Rockingham 7",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:rockingham_7",
            ),
            District(
                "Rockingham 8",
                "lower",
                9,
                "ocd-division/country:us/state:nh/sldl:rockingham_8",
            ),
            District(
                "Rockingham 9",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:rockingham_9",
            ),
            District(
                "Rockingham 10",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_10",
            ),
            District(
                "Rockingham 11",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_11",
            ),
            District(
                "Rockingham 12",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_12",
            ),
            District(
                "Rockingham 13",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:rockingham_13",
            ),
            District(
                "Rockingham 14",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:rockingham_14",
            ),
            District(
                "Rockingham 15",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_15",
            ),
            District(
                "Rockingham 16",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_16",
            ),
            District(
                "Rockingham 17",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:rockingham_17",
            ),
            District(
                "Rockingham 18",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:rockingham_18",
            ),
            District(
                "Rockingham 19",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:rockingham_19",
            ),
            District(
                "Rockingham 20",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:rockingham_20",
            ),
            District(
                "Rockingham 21",
                "lower",
                4,
                "ocd-division/country:us/state:nh/sldl:rockingham_21",
            ),
            District(
                "Rockingham 22",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_22",
            ),
            District(
                "Rockingham 23",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_23",
            ),
            District(
                "Rockingham 24",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:rockingham_24",
            ),
            District(
                "Rockingham 25",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_25",
            ),
            District(
                "Rockingham 26",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_26",
            ),
            District(
                "Rockingham 27",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_27",
            ),
            District(
                "Rockingham 28",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_28",
            ),
            District(
                "Rockingham 29",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_29",
            ),
            District(
                "Rockingham 30",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_30",
            ),
            District(
                "Rockingham 31",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_31",
            ),
            District(
                "Rockingham 32",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_32",
            ),
            District(
                "Rockingham 33",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_33",
            ),
            District(
                "Rockingham 34",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_34",
            ),
            District(
                "Rockingham 35",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_35",
            ),
            District(
                "Rockingham 36",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_36",
            ),
            District(
                "Rockingham 37",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:rockingham_37",
            ),
            District(
                "Strafford 1",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:strafford_1",
            ),
            District(
                "Strafford 2",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:strafford_2",
            ),
            District(
                "Strafford 3",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:strafford_3",
            ),
            District(
                "Strafford 4",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:strafford_4",
            ),
            District(
                "Strafford 5",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_5",
            ),
            District(
                "Strafford 6",
                "lower",
                5,
                "ocd-division/country:us/state:nh/sldl:strafford_6",
            ),
            District(
                "Strafford 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_7",
            ),
            District(
                "Strafford 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_8",
            ),
            District(
                "Strafford 9",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_9",
            ),
            District(
                "Strafford 10",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_10",
            ),
            District(
                "Strafford 11",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_11",
            ),
            District(
                "Strafford 12",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_12",
            ),
            District(
                "Strafford 13",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_13",
            ),
            District(
                "Strafford 14",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_14",
            ),
            District(
                "Strafford 15",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_15",
            ),
            District(
                "Strafford 16",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_16",
            ),
            District(
                "Strafford 17",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:strafford_17",
            ),
            District(
                "Strafford 18",
                "lower",
                3,
                "ocd-division/country:us/state:nh/sldl:strafford_18",
            ),
            District(
                "Strafford 19",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_19",
            ),
            District(
                "Strafford 20",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_20",
            ),
            District(
                "Strafford 21",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_21",
            ),
            District(
                "Strafford 22",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_22",
            ),
            District(
                "Strafford 23",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_23",
            ),
            District(
                "Strafford 24",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_24",
            ),
            District(
                "Strafford 25",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:strafford_25",
            ),
            District(
                "Sullivan 1",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:sullivan_1",
            ),
            District(
                "Sullivan 2",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_2",
            ),
            District(
                "Sullivan 3",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_3",
            ),
            District(
                "Sullivan 4",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_4",
            ),
            District(
                "Sullivan 5",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_5",
            ),
            District(
                "Sullivan 6",
                "lower",
                2,
                "ocd-division/country:us/state:nh/sldl:sullivan_6",
            ),
            District(
                "Sullivan 7",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_7",
            ),
            District(
                "Sullivan 8",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_8",
            ),
            District(
                "Sullivan 9",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_9",
            ),
            District(
                "Sullivan 10",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_10",
            ),
            District(
                "Sullivan 11",
                "lower",
                1,
                "ocd-division/country:us/state:nh/sldl:sullivan_11",
            ),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        num_seats=24,
        title="Senator",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:nh", "upper", 24
        ),
    ),
)
