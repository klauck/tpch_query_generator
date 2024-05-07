import os

from query_generator import QueryGenerator


def main():
    for query_id in range(22):
        with open(os.path.join(os.path.dirname(__file__), f'query_templates/{query_id + 1}.sql')) as query_template_file:
            print(f'############ QUERY {query_id + 1} ############')
            print(QueryGenerator.generate_query(query_template_file.read(),
                                                 query_id + 1,
                                                 should_validate=True,
                                                 scale_factor=1,
                                                 stream_id=0))
            print('\n\n')


if __name__ == '__main__':
    main()
