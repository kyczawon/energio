import os
directory='/Users/leszek/Desktop/Desktop/Imperial/FYP/monkey'

current = [x for x in os.walk(directory)][0]

# go through the folder and make tasks named after the name of the folder
for task in current[1]:
    new_task = Task(benchmark=benchmark_id, name = name)
    new_task.save()

    current2 = [x for x in os.walk(directory+'/'+task)][0]

    # go through each folder and make app named after the file name without the extension
    for filename in current2[2]:
        app, _ = os.path.splitext(filename)

        exisitng_apps = App.objects.filter(benchmark=benchmark_id).values_list('name', flat=True)
        
        # avoid creating duplicate apps
        if app not in exisitng_apps:
            new_app = App(benchmark=benchmark_id, name = app)
            new_task.save()