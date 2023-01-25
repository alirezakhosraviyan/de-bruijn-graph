import click
from lib.de_bruijn_graph import draw_de_bruijn_graph, create_de_bruijn_graph
from lib.tools import fit_polynomial_and_draw, get_robustness, calc_monte
import time


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
@click.option("-n", "--nodes", required=True, help="the number of nodes", type=int)
@click.option("-e", "--edges", required=True, help="the number of edges", type=int)
def show_robustness(nodes, edges):
    the_graph = create_de_bruijn_graph(nodes, edges)
    res = get_robustness(the_graph)

    click.echo(f"Robustness: \n {res}")


@click.command(name="simulate")
@click.option("-n", "--nodes", required=True, help="the number of nodes", type=int)
@click.option("-e", "--edges", required=True, help="the number of edges", type=int)
@click.option("-s", "--simulation", required=True, help="the number of edges", type=int)
def simulate(nodes, edges, simulation):
    by_probability = [[] for _ in range(10)]

    start_time = time.time()
    for sim in range(simulation):
        for n in range(nodes, edges):
            for k in range(nodes, edges):
                p, F, R = calc_monte((k, n))
                by_probability[int(p * 10)].append((F, R))

    click.echo(f"Simulation completed for {simulation} in {time.time() - start_time} seconds")
    for rfs in by_probability:
        fit_polynomial_and_draw(rfs)


run.add_command(show_de_bru)
run.add_command(show_robustness)
run.add_command(simulate)


if __name__ == '__main__':
    run()
