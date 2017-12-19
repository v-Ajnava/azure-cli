from azure.mgmt.servicebus.models.service_bus_management_client_enums import SkuName, SkuTier, AccessRights


def skunameconverter(skuname):

    if skuname == 'Basic':
        return SkuName.basic
    if skuname == 'Standard':
        return SkuName.standard
    if skuname == 'Premium':
        return SkuName.premium


def skutireconverter(skutire):

    if skutire == 'Basic':
        return SkuTier.basic
    if skutire == 'Standard':
        return SkuTier.standard
    if skutire == 'Premium':
        return SkuTier.premium


def accessrights_converter(accessrights):
    if len(accessrights) > 0:
        accessrights_new = []
        for index in accessrights:
            if index == 'Send':
                accessrights_new.append(AccessRights.send)
            if accessrights[index] == 'Manage':
                accessrights_new.append(AccessRights.manage)
            if accessrights[index] == 'Listen':
                accessrights_new.append(AccessRights.listen)

        return accessrights
