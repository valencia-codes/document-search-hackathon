import click
@click.command()
@click.option('--query', prompt='What would you like to know?')

def run_document_search(query):
    # Run the document search in here
    response = 'response'
    click.echo(response)

if __name__ == "__main__":
    run_document_search()