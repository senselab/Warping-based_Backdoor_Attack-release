import argparse


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_root", type=str, default="/home/ubuntu/temps/")
    parser.add_argument("--checkpoints", type=str, default="./checkpoints")
    parser.add_argument("--temps", type=str, default="./temps")
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--continue_training", action="store_true")
    parser.add_argument("--saving_prefix", type=str, help="Folder in /checkpoints for saving ckpt")

    parser.add_argument("--dataset", type=str, default="cifar10")
    parser.add_argument("--input_height", type=int, default=None)
    parser.add_argument("--input_width", type=int, default=None)
    parser.add_argument("--input_channel", type=int, default=None)
    parser.add_argument("--num_classes", type=int, default=None)
    parser.add_argument("--attack_mode", type=str, default="all2one")

    parser.add_argument("--bs", type=int, default=128)
    parser.add_argument("--lr_C", type=float, default=1e-2)
    parser.add_argument("--schedulerC_milestones", type=list, default=[100, 200, 300, 400])
    parser.add_argument("--schedulerC_lambda", type=float, default=0.1)
    parser.add_argument("--n_iters", type=int, default=1000)
    parser.add_argument("--num_workers", type=float, default=6)

    parser.add_argument("--lambda_grid", type=float, default=0.2)
    parser.add_argument("--target_label", type=int, default=0)
    parser.add_argument("--pc", type=float, default=0.03)
    parser.add_argument("--cross_ratio", type=float, default=1.5)

    parser.add_argument("--random_rotation", type=int, default=10)
    parser.add_argument("--random_crop", type=int, default=5)

    parser.add_argument("--scale", type=float, default=1)
    parser.add_argument("--k", type=int, default=4)  # low-res grid size
    parser.add_argument(
        "--grid-rescale", type=float, default=1
    )  # scale grid values to avoid going out of [-1, 1]. For example, grid-rescale = 0.98
    parser.add_argument("--clamp", action="store_true")  # clamp grid values to [-1, 1]
    parser.add_argument("--nearest", type=int, default=0)  # control grid round-up precision
    #     0: No round-up, just use interpolated input values   (smooth, blur)
    #     1: Round-up to pixel precision                       (sharp, noisy)
    #     2: Round-up to 1/2 pixel precision                   (moderate)

    return parser