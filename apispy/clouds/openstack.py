from novaclient.v1_1 import client


class OpenStack:
    def __init__(self, user, password, tenant, auth_url, region):
        self.auth_url = auth_url
        self.password = password
        self.region = region
        self.tenant = tenant
        self.user = user

        self.client = client.Client(user, password, tenant, auth_url,
                                    region_name=region)

        self.flavors = []
        self.images = []
        self.keypairs = []
        self.networks = []
        self.servers = []
        self.volumes = []

    # Things to pull from the OpenStack object
    def auth_url(self):
        return self.auth_url

    def client(self):
        return self.client

    def region(self):
        return self.region

    def tenant(self):
        return self.tenant

    def user(self):
        return self.user

    # Things to pull from the API

    def get_flavors(self):
        self.flavors = _to_dict(self.client.flavors.list())
        return self.flavors

    def get_images(self):
        self.images = _to_dict(self.client.images.list())
        return self.images

    def get_keypairs(self):
        self.keypairs = _to_dict(self.client.keypairs.list(), "keypair")
        return self.keypairs

    def get_networks(self):
        self.networks = _to_dict(self.client.networks.list())
        return self.networks

    def get_servers(self):
        self.servers = _to_dict(self.client.servers.list())
        return self.servers

    def get_volumes(self):
        self.volumes = _to_dict(self.client.volumes.list())
        return self.volumes


def _to_dict(values, key=None):
    v = []
    for value in values:
        if key:
            v.append(value.to_dict()[key])
        else:
            v.append(value.to_dict())
    return v
