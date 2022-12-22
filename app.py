import requests
from bs4 import BeautifulSoup
import csv


# link = input('pls enter the link: ')
link = 'https://www.yallakora.com/match-center/?date=12/14/2022'

html = requests.get(link)


def main(html):
    src = html.content
    soup = BeautifulSoup(src, 'lxml')
    matches_details = []

    championlegs = soup.find_all('div', {'class': 'matchCard'})

    def get_match(championlegs):
        matche_title = championlegs.contents[1].find('h2').text.strip()
        all_matches = championlegs.contents[3].find_all('li')
        matches_num = len(all_matches)

        for i in range(matches_num):

            # Get Teames Name
            team_A = all_matches[i].find(
                'div', {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find(
                'div', {'class': 'teamB'}).text.strip()

            # Get Score
            match_result = all_matches[i].find(
                'div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # Get Match Time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find(
                'span', {'class': 'time'}).text.strip()

            # Add Data to Empty List(matches_details = [])
            matches_details.append({
                "البطولة": matche_title,
                "الفريق الأول": team_A,
                "الفريق الثاني": team_B,
                "التوقيت": match_time,
                "النتيجة": score
            })

    for i in range(len(championlegs)):
        get_match(championlegs[i])

    keys = matches_details[0].keys()

    # Save data as .csv file in the same folder
    with open('file.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print('Done...')


main(html)
