#! /usr/bin/python3
import random
import argparse


def simulate_epidemic(nodes_count, iterations_count, x=4):
    success_count = 0
    for i in range(iterations_count):
        nodes_which_receive = [False] * nodes_count
        cur_nodes = [0]
        next_nodes = []
        while cur_nodes:
            for node in cur_nodes:
                if not nodes_which_receive[node]:
                    nodes_which_receive[node] = True
                    next_nodes += random.sample(range(nodes_count), x)
            cur_nodes = next_nodes
            next_nodes = []
        success_count += all(nodes_which_receive)
    return 100 * success_count / iterations_count


# every node which have already received packet continues
# sending packet to random nodes until it will receive packet
# again
def advanced_epidemic(nodes_count, iterations_count, x=4):
    success_count = 0
    for i in range(iterations_count):
        nodes_which_receive = [False] * nodes_count
        nodes_which_receive_again = [False] * nodes_count
        cur_nodes = [0]
        next_nodes = []
        while cur_nodes:
            for node in cur_nodes:
                if not nodes_which_receive[node]:
                    nodes_which_receive[node] = True
                    next_nodes += random.sample(range(nodes_count), x)
                elif not nodes_which_receive_again[node]:
                    next_nodes.append(node)
                    nodes_which_receive_again[node] = True
                    next_nodes += random.sample(range(nodes_count), x)
            cur_nodes = next_nodes
            next_nodes = []
        success_count += all(nodes_which_receive)
    return 100 * success_count / iterations_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, dest='nodes_count', required=True)
    parser.add_argument('-i', type=int, dest='iterations_count', required=True)
    parser.add_argument('--your-algorithm', action='store_true', dest='advanced_algorithm')
    args = parser.parse_args()
    if args.advanced_algorithm:
        success_percent = advanced_epidemic(args.nodes_count, args.iterations_count)
    else:
        success_percent = simulate_epidemic(args.nodes_count, args.iterations_count)
    print("In %.2f%% cases all nodes received the packet" % success_percent)


if __name__ == '__main__':
    main()
