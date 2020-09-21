import argparse
import json
import os





'''
for k, v in sorted(vars(opt).items()):
            comment = ''
            default = self.parser.get_default(k)
            if v != default:
                comment = '\t[default: %s]' % str(default)
            message += '{:>25}: {:<30}{}\n'.format(str(k), str(v), comment)
        message += '----------------- End -------------------'

'''

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--data_root',type=str, default='data')
parser.add_argument('--data_root2',type=str, default='data2')
opt=parser.parse_args()
print(opt)
print(type(opt.data_root))

opt.data_root='data2'
opt.data_root3='data3'
print(opt)

with open('opt2.txt','w') as outfile:
    outfile.write(json.dumps(vars(opt),indent=2))

print(" ")
opt_log = os.path.join('opt.txt')
with open(opt_log) as datafile:
    data_loaded=json.load(datafile)
print(data_loaded)
print(data_loaded['dataroot'])
print(len(data_loaded))
print(data_loaded.items())
for (k0, v0) ,(kn,vn) in zip(sorted(data_loaded.items()),sorted(data_loaded.items())):
    #print(k0,':',v0,',',kn,':',vn)
    if k0==kn and vn !=v0:
        print(k0,':',v0,' -> ',vn)
        print(type(k0))