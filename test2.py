import requests
from pprint import pprint


class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url

    # 제목으로 영화 검색 후, 검색결과에서 id를 찾아서 return
    def get_movie_id(self, title):
        request_url = self.get_request_url('/search/movie',
                                           query=title, region='KR', language='ko')
        # 검색 결과 dict
        data = requests.get(request_url).json()
        results = data.get('results')

        if results:
            movie_id = results[0]['id']
        else:
            return None

        return movie_id


tmdb_helper = TMDBHelper('0cdf5d1b00a1a5e72e99fbb30ff4ec91')
