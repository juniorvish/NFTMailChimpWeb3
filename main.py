```python
from underdog_protocol import UnderdogProtocolAPI
from dispatch_api import DispatchAPI
from synap_api import SynapAPI
from create_lists import create_lists
from collect_wallets import collect_wallet_addresses
from embeddable_form import EmbeddableForm
from upload_csv import upload_csv
from view_cnfts import view_cnfts
from interface import Interface
from send_nfts import send_nfts
from draft_message import draft_message
from marketing_campaigns import MarketingCampaigns
from dust_cnfts import dust_cnfts
from measure_actions import measure_actions
from token_gating import token_gating
from check_open import check_open
from utm_parameters import utm_parameters
from automate_drop import automate_drop
from create_project import create_project
from import_wallets import import_wallets
from dust_wallets import dust_wallets
from user_login import user_login
from confirm_message import confirm_message
from game import Game
from check_analytics import check_analytics
from dashboard import Dashboard
from on_chain_stamps import on_chain_stamps

def main():
    underdog_api = UnderdogProtocolAPI()
    dispatch_api = DispatchAPI()
    synap_api = SynapAPI()

    # Create lists
    create_lists(underdog_api)

    # Collect wallet addresses
    wallet_addresses = collect_wallet_addresses()

    # Embeddable form
    form = EmbeddableForm()

    # Upload CSV
    upload_csv(wallet_addresses)

    # View cNFTs
    view_cnfts(synap_api)

    # Interface
    interface = Interface(dispatch_api)

    # Send NFTs
    send_nfts(underdog_api, wallet_addresses)

    # Draft message
    draft_message(interface)

    # Marketing Campaigns
    campaigns = MarketingCampaigns()

    # Dust cNFTs
    dust_cnfts(underdog_api, wallet_addresses)

    # Measure actions
    measure_actions()

    # Token Gating
    token_gating(wallet_addresses)

    # Check open
    check_open()

    # UTM parameters
    utm_parameters()

    # Automate drop
    automate_drop()

    # Create project
    create_project(underdog_api)

    # Import wallets
    import_wallets(wallet_addresses)

    # Dust wallets
    dust_wallets(underdog_api, wallet_addresses)

    # User login
    user_login()

    # Confirm message
    confirm_message()

    # Game
    game = Game()

    # Check analytics
    check_analytics()

    # Dashboard
    dashboard = Dashboard()

    # On-chain stamps
    on_chain_stamps()

if __name__ == "__main__":
    main()
```