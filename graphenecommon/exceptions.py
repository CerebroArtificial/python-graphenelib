__all__ = [
    "InvalidWifError",
    "KeyAlreadyInStoreException",
    "KeyNotFound",
    "NoWalletException",
    "OfflineHasNoRPCException",
    "WalletExists",
    "WalletLocked",
]


class WalletExists(Exception):
    """ A wallet has already been created and requires a password to be
        unlocked by means of :func:`bitshares.wallet.unlock`.
    """

    pass


class WalletLocked(Exception):
    """ Wallet is locked
    """

    pass


class OfflineHasNoRPCException(Exception):
    """ When in offline mode, we don't have RPC
    """

    pass


class NoWalletException(Exception):
    """ No Wallet could be found, please use :func:`bitshares.wallet.create` to
        create a new wallet
    """

    pass


class KeyNotFound(Exception):
    """ Key not found
    """

    pass


class KeyAlreadyInStoreException(Exception):
    """ The key is already stored in the store
    """

    pass


class InvalidWifError(Exception):
    """ The provided private Key has an invalid format
    """

    pass


class WorkerDoesNotExistsException(Exception):
    pass


class WitnessDoesNotExistsException(Exception):
    pass


class VestingBalanceDoesNotExistsException(Exception):
    pass


class InsufficientAuthorityError(Exception):
    pass


class InvalidWifError(Exception):
    pass


class MissingKeyError(Exception):
    pass


class WalletLocked(Exception):
    pass


class AssetDoesNotExistsException(Exception):
    pass


class AccountDoesNotExistsException(Exception):
    pass


class AssetDoesNotExistsException(Exception):
    pass


class InvalidAssetException(Exception):
    pass


class BlockDoesNotExistsException(Exception):
    pass


class CommitteeMemberDoesNotExistsException(Exception):
    pass


class KeyNotFound(Exception):
    pass


class MissingKeyError(Exception):
    pass


class InvalidMemoKeyException(Exception):
    pass


class InvalidMessageSignature(Exception):
    pass


class WrongMemoKey(Exception):
    pass


class ProposalDoesNotExistException(Exception):
    pass
