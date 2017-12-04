This process assume that a roscore is running, the correct ROS_MASTER_URI is set, and data is already pulled from the refnet and published to ROS.

To launch the PP stack, first make sure the configuration files for the quad are correct. 

1) Edit quad.launch and change the node name and namespace parameter to correspond to the quad's name
2) Edit launch_ppfusion and change the quad gbx topic and output topic to the quad's name

To run the program, simply type:
./launch_stack

It will launch a tmux session with all of the programs running inside it.
