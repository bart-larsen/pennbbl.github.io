import flywheel
import datetime

fw = flywheel.Client()

qsiprep = fw.lookup('gears/qsiprep-fw-hpc')
project = fw.projects.find_first("label=gear_testing")

now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
analysis_label = 'exampleanalysis_{}_{}_{}'.format(qsiprep.gear.name,qsiprep.gear.version, now)

config = {
            "hmc_model": "eddy",
            "use_syn_sdc": False,
            'b0_threshold': 100,
            'save_outputs': True,
            'dwi_denoise_window': 5,
            'do_reconall': False,
            'b0_to_t1w_transform': 'Rigid',
            'combine_all_dwis': False,
            'intramodal_template_iters': 0,
            'force_spatial_normalization': True,
            'shoreline_iters': 0,
            'output_resolution': 1.5,
            'output_space': 'T1w',
            'sloppy': True,
            'unringing_method': 'mrdegibbs'
        }

inputs = {
    "freesurfer_license": project.files[2],
}

sessions_to_run = []
for session in project.sessions():
    desired_session = 'acq-64dir_dwi' in [acq.label for acq in session.acquisitions()]
    if desired_session
        sessions_to_run.append(session)

analysis_ids = []
fails = []
for ses in sessions_to_run:
    try:
        _id = qsiprep.run(analysis_label=analysis_label,
                          config=config, inputs=inputs, destination=ses)
        analysis_ids.append(_id)
    except Exception as e:
        print(e)
        fails.append(ses)
