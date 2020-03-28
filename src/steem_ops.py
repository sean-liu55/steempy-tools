from steem import Steem
from steem.transactionbuilder import TransactionBuilder
from steembase import operations
import json
import sys

nodes_remote = ["https://api.steemit.com"]


def withdraw():
    with open("config/config_withdraw.json", 'r') as load_f:
        input_args = json.load(load_f)

    for i in range(len(input_args)):
        args = input_args[i]

        key = args['key']
        withdraw_vesting_object = args['withdraw_vesting']
        account_name = withdraw_vesting_object['account']

        steem = Steem(nodes=nodes_remote, keys=key)

        # now we can construct the transaction
        # we will set no_broadcast to True because
        # we don't want to really send funds, just testing.
        tb = TransactionBuilder()

        # lets serialize our transfers into a format Steem can understand
        operationsList = []
        operationsList.append(operations.WithdrawVesting(**withdraw_vesting_object))

        # do SetWithdrawVestingRoute
        if 'SetWithdrawVestingRouteList' in args:
            SetWithdrawVestingRouteList = args['SetWithdrawVestingRouteList']
            len_item = len(SetWithdrawVestingRouteList)
            for i in range(len_item):
                set_route_parameters = SetWithdrawVestingRouteList[i]
                operationsList.append(operations.SetWithdrawVestingRoute(**set_route_parameters))

        # tell TransactionBuilder to use our serialized transfers
        tb.appendOps(operationsList)

        # we need to tell TransactionBuilder about
        # everyone who needs to sign the transaction.
        tb.appendSigner(account_name, 'active')

        # sign the transaction
        tb.sign()

        # broadcast the transaction (publish to steem)
        # since we specified no_broadcast=True earlier
        # this method won't actually do anything
        tx = tb.broadcast()


def delegate_vest():
    with open("config/config_delegate_vest.json", 'r') as load_f:
        input_args = json.load(load_f)

    for i in range(len(input_args)):
        args = input_args[i]

        key = args['key']
        operation_object = args['delegate_vest']
        account_name = operation_object['delegator']

        steem = Steem(nodes=nodes_remote, keys=key)

        # now we can construct the transaction
        # we will set no_broadcast to True because
        # we don't want to really send funds, just testing.
        tb = TransactionBuilder()

        # lets serialize our transfers into a format Steem can understand
        operationsList = []
        operationsList.append(operations.DelegateVestingShares(**operation_object))

        # tell TransactionBuilder to use our serialized transfers
        tb.appendOps(operationsList)

        # we need to tell TransactionBuilder about
        # everyone who needs to sign the transaction.
        # since all payments are made from `richguy`,
        # we just need to do this once
        tb.appendSigner(account_name, 'active')

        # sign the transaction
        tb.sign()

        # broadcast the transaction (publish to steem)
        # since we specified no_broadcast=True earlier
        # this method won't actually do anything
        tx = tb.broadcast()

        print(account_name + " done")


def vote_witness():
    with open("config_vote_witness.json", 'r') as load_f:
        input_args = json.load(load_f)

    for i in range(len(input_args)):
        args = input_args[i]

        key = args['key']
        operation_object = args['vote_witness']
        account_name = operation_object['account']

        steem = Steem(nodes=nodes_remote, keys=key)

        # now we can construct the transaction
        # we will set no_broadcast to True because
        # we don't want to really send funds, just testing.
        tb = TransactionBuilder()

        # lets serialize our transfers into a format Steem can understand
        operationsList = []
        operationsList.append(operations.AccountWitnessVote(**operation_object))

        # tell TransactionBuilder to use our serialized transfers
        tb.appendOps(operationsList)

        # we need to tell TransactionBuilder about
        # everyone who needs to sign the transaction.
        # since all payments are made from `richguy`,
        # we just need to do this once
        tb.appendSigner(account_name, 'active')

        # sign the transaction
        tb.sign()

        # broadcast the transaction (publish to steem)
        # since we specified no_broadcast=True earlier
        # this method won't actually do anything
        tx = tb.broadcast()

        print(account_name + " done")


def update_account():
    with open("config_update_account.json", 'r') as load_f:
        input_args = json.load(load_f)

    for i in range(len(input_args)):
        args = input_args[i]

        key = args['key']
        update_account_object = args['update_account']
        account_name = update_account_object['account']

        steem = Steem(nodes=nodes_remote, keys=key)

        # now we can construct the transaction
        # we will set no_broadcast to True because
        # we don't want to really send funds, just testing.
        tb = TransactionBuilder()

        # lets serialize our transfers into a format Steem can understand
        operationsList = []
        operationsList.append(operations.AccountUpdate(**update_account_object))

        # tell TransactionBuilder to use our serialized transfers
        tb.appendOps(operationsList)

        # we need to tell TransactionBuilder about
        # everyone who needs to sign the transaction.
        # since all payments are made from `richguy`,
        # we just need to do this once
        tb.appendSigner(account_name, 'owner')

        # sign the transaction
        tb.sign()

        # broadcast the transaction (publish to steem)
        # since we specified no_broadcast=True earlier
        # this method won't actually do anything
        tx = tb.broadcast()

        print(account_name + " done")


def update_witness():
    with open("config_update_witness.json", 'r') as load_f:
        input_args = json.load(load_f)

    for i in range(len(input_args)):
        args = input_args[i]

        key = args['key']
        update_account_object = args['update_witness']
        account_name = update_account_object['owner']

        steem = Steem(nodes=nodes_remote, keys=key)

        # now we can construct the transaction
        # we will set no_broadcast to True because
        # we don't want to really send funds, just testing.
        tb = TransactionBuilder()

        # lets serialize our transfers into a format Steem can understand
        operationsList = []
        operationsList.append(operations.WitnessUpdate(**update_account_object))

        # tell TransactionBuilder to use our serialized transfers
        tb.appendOps(operationsList)

        # we need to tell TransactionBuilder about
        # everyone who needs to sign the transaction.
        # since all payments are made from `richguy`,
        # we just need to do this once
        tb.appendSigner(account_name, 'owner')

        # sign the transaction
        tb.sign()

        # broadcast the transaction (publish to steem)
        # since we specified no_broadcast=True earlier
        # this method won't actually do anything
        tx = tb.broadcast()

        print(account_name + " done")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("argv num must be 1.")
        sys.exit(-1)

    op_str = str(sys.argv[1])

    if op_str == 'update_account':
        update_account()
    elif op_str == 'update_witness':
        update_witness()
    elif op_str == 'withdraw':
        withdraw()
    elif op_str == 'delegate_vest':
        delegate_vest()
    elif op_str == 'vote_witness':
        vote_witness()
    else:
        print("input op error")
        print("support op: update_account、update_witness、withdraw、delegate_vest、vote_witness")
        sys.exit(-1)

    print("done")
    sys.exit(0)
