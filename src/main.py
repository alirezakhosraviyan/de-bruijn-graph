import click
from lib.de_bruijn_graph import draw_de_bruijn_graph, create_de_bruijn_graph
from lib.tools import fit_polynomial_and_draw, get_robustness, monte_carlo


@click.group()
def run():
    """main function for commands"""


@click.command(name="show-de-bru")
@click.option("-n", "--nodes", required=True, help="the number of nodes", type=int)
@click.option("-e", "--edges", required=True, help="the number of edges", type=int)
def show_de_bru(nodes, edges):
    print(nodes, edges)
    the_graph = create_de_bruijn_graph(nodes, edges)
    draw_de_bruijn_graph(the_graph)


@click.command(name="show-robustness")
@click.option("-n", "--nodes", required=True, help="the number of nodes")
@click.option("-e", "--edges", required=True, help="the number of edges")
def show_robustness(nodes, edges):
    the_graph = create_de_bruijn_graph(nodes, edges)
    res = get_robustness(the_graph)

    click.echo(f"Robustness: \n {res}")


@click.command(name="simulate")
@click.option("-n", "--nodes", required=True, help="the number of nodes", type=int)
@click.option("-e", "--edges", required=True, help="the number of edges", type=int)
@click.option("-s", "--simulation", required=True, help="the number of edges", type=int)
def simulate(nodes, edges, simulation):
    # by_probability represents the (F, R) tuple for 10 different cases of probability
    # by_probability[0] corresponds to probability between 0.0 -> 0.1
    # by_probability[1] corresponds to probability between 0.1 -> 0.2 and etc.
    by_probability = [[] for _ in range(10)]
    for epoch in range(simulation):
        for n in range(2, 5):
            for k in range(2, 5):
                p, F, R = monte_carlo((k, n))
                by_probability[int(p * 10)].append((F, R))
        print(f'Epoch {epoch} has successfully completed!')

    for rfs in by_probability:
        fit_polynomial_and_draw(rfs)


run.add_command(show_de_bru)
run.add_command(show_robustness)
run.add_command(simulate)


if __name__ == '__main__':
    run()
