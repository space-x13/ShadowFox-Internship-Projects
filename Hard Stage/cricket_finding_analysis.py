import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# Function to fetch and parse match data
def fetch_match_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Function to extract player names to analyze
def get_players_to_analyze(soup):
    players_to_analyse = []
    score_card = soup.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")
    for names in score_card:
        players = names.find_all('a', class_="cb-text-link")
        for player in players:
            players_to_analyse.append(player.text.strip())
    return players_to_analyse[:3]

# Function to collect fielding events
def collect_fielding_events(soup, players_to_analyse):
    fielding_events = {player: [] for player in players_to_analyse}
    commentary = soup.find_all('div', class_="cb-col cb-col-100 cb-col-rt")

    for ball in commentary:
        ball_info = ball.find('div', class_="cb-col cb-col-100 cb-scrd-itms")
        if ball_info:
            ball_news = ball_info.text.strip()
            if ball_news:
                descriptions = ball_news.split(', ')
                over = descriptions[0].split(' ')[0]
                for player in players_to_analyse:
                    if player in ball_news:
                        event_type = None
                        effectiveness = None
                        if 'caught' in ball_news:
                            event_type = 'caught'
                            effectiveness = 'successful' if 'out' in ball_news else 'unsuccessful'
                        elif 'run-out' in ball_news:
                            event_type = 'run-out'
                            effectiveness = 'successful' if 'out' in ball_news else 'unsuccessful'
                        elif 'misfield' in ball_news:
                            event_type = 'misfield'
                            effectiveness = 'unsuccessful'
                        elif 'saved' in descriptions:
                            event_type = 'boundary_saved'
                            effectiveness = 'successful'
                        if event_type:
                            fielding_events[player].append({'over': over, 'type': event_type, 'effectiveness': effectiveness})
    return fielding_events

# Function to save fielding data to Excel
def save_fielding_data(fielding_events):
    fielding_data = []
    for player, events in fielding_events.items():
        for event in events:
            fielding_data.append({
                'Player': player,
                'Over': event['over'],
                'Type': event['type'],
                'Effectiveness': event['effectiveness']
            })
    df = pd.DataFrame(fielding_data)
    df.to_excel('fielding_data.xlsx', index=False)
    print("Fielding data compiled into 'fielding_data.xlsx'")

# Function to analyze fielding performance
def analyze_fielding_performance(fielding_events):
    for player, events in fielding_events.items():
        total_events = len(events)
        successful_events = sum([1 for e in events if e['effectiveness'] == 'successful'])
        success_rate = (successful_events / total_events) * 100 if total_events > 0 else 0

        print(f"Fielding Performance for {player}")
        print(f"Total Fielding Events: {total_events}")
        print(f"Successful Events: {successful_events}")
        print(f"Success Rate: {success_rate:.2f}%")
        print("Detailed Events:")
        for result in events:
            print(f'    Over: {result["over"]}, Type: {result["type"]}, Effectiveness: {result["effectiveness"]}')
        print('')

        total_catches = sum([1 for e in events if e['type'] == 'caught'])
        total_run_outs = sum([1 for e in events if e['type'] == 'run-out'])
        total_misfields = sum([1 for e in events if e['type'] == 'misfield'])
        total_boundary_saved = sum([1 for e in events if e['type'] == 'boundary_saved'])
        total_errors = total_misfields

        print(f'Total Catches: {total_catches}')
        print(f'Total Run Outs: {total_run_outs}')
        print(f'Total Misfields: {total_misfields}')
        print(f'Total Boundary Saved: {total_boundary_saved}')
        print(f'Total Errors: {total_errors}')
        print('')

# Function to visualize fielding performance
def visualize_fielding_performance(fielding_events):
    players = fielding_events.keys()
    total_events = [len(events) for events in fielding_events.values()]
    successful_events = [sum([1 for e in events if e['effectiveness'] == 'successful']) for events in fielding_events.values()]

    plt.bar(players, total_events, label='Total Events')
    plt.bar(players, successful_events, label='Successful Events', bottom=[total - successful for total, successful in zip(total_events, successful_events)])
    plt.xlabel('Players')
    plt.ylabel('Number of Events')
    plt.title('Fielding Performance')
    plt.legend()
    plt.show()

    for player, events in fielding_events.items():
        over_numbers = [int(event['over']) for event in events]
        unique_overs = sorted(set(over_numbers))
        success_rate_over = [
            sum([1 for event in events if event['effectiveness'] == 'successful' and int(event['over']) == over]) /
            len([event for event in events if int(event['over']) == over]) * 100
            for over in unique_overs
        ]
        plt.plot(unique_overs, success_rate_over, label=f'{player} Success Rate')

    plt.xlabel('Over')
    plt.ylabel('Success Rate (%)')
    plt.title('Success Rate Over Time')
    plt.legend()
    plt.show()

# Main script execution
def main():
    url = "https://www.cricbuzz.com/live-cricket-scorecard/12345/match-name"
    soup = fetch_match_data(url)
    players_to_analyze = get_players_to_analyze(soup)
    fielding_events = collect_fielding_events(soup, players_to_analyze)
    save_fielding_data(fielding_events)
    analyze_fielding_performance(fielding_events)
    visualize_fielding_performance(fielding_events)

if __name__ == "__main__":
    main()
