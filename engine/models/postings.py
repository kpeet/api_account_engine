from django.db import models
from engine.models.abstract_model import AbstractModel
from engine.models.accounts import Account
from engine.models.journals import Journal


class AssetType(AbstractModel):
    description = models.CharField(max_length=150)


class Posting(AbstractModel):
    account = models.ForeignKey(Account, null=False, on_delete=models.PROTECT)
    journal = models.ForeignKey(Journal, null=False, on_delete=models.PROTECT, related_name='postings')
    amount = models.DecimalField(null=False, default=0, max_digits=20, decimal_places=5)
    asset_type = models.ForeignKey(AssetType, default=1, null=False, on_delete=models.PROTECT)
