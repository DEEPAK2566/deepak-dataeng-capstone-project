import numpy as np
import pandas as pd

def load_players(file_path):
    return pd.read_csv(file_path)

def load_matches(file_path):
    return pd.read_csv(file_path)   

def merge_players_matches(players_df, matches_df):
   merged = pd.merge(players_df, matches_df, on="PlayerID")
   return merged
   

def total_runs_per_team(merged_df):
    df=  merged_df.groupby('Team',as_index=False)['Runs'].sum()
    return df
   

def calculate_strike_rate(merged_df):
    merged_df['StrikeRate']=100
    result=merged_df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]
    return result
    

def runs_agg_per_player(merged_df):
    df = merged_df.groupby(["PlayerID","Name"])["Runs"].agg(["mean", "max", "min"]).reset_index()
    return df

def avg_age_by_role(players_df):
   df = players_df.groupby("Role", as_index=False)["Age"].mean()
   return df
   
def total_matches_per_player(matches_df):
    df = matches_df.groupby("PlayerID").size()
    df =df.reset_index(name="MatchCount")
    return df

    # Step 1: Get counts (index: PlayerID, column: count)
    # Step 2: Rename columns explicitly and cleanly
    # Ensure columns are in correct order
   

def top_wicket_takers(merged_df):
    df=merged_df.groupby(["PlayerID","Name"],as_index=False)["Wickets"].sum()
    df_top = df.sort_values("Wickets",ascending=False).head(3)
    return df_top
    

def avg_strike_rate_per_team(merged_df):
    df=merged_df.groupby("Team",as_index=False)["StrikeRate"].mean()
    return df

def catch_to_match_ratio(merged_df):
    catch=merged_df.groupby("PlayerID",as_index=False)["Catches"].sum()
    match = merged_df.groupby("PlayerID").size().reset_index(name="MatchCount")
    df = pd.merge(catch,match,on="PlayerID")
    df["CatchToMatchRatio"] = df["Catches"] / df["MatchCount"]
    result = df[["PlayerID", "CatchToMatchRatio"]]
    return result












